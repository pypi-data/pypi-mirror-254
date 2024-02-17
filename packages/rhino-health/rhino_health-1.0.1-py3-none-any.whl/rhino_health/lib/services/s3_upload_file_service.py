import base64
import hashlib
import math
import os
import shutil
import tempfile
import zipfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Dict

import requests

MIN_PART_SIZE = 5 * 1024 * 1024  # 5MB
MAX_PART_SIZE = 100 * 1024 * 1024  # 100MB
MAX_CHUNK_SIZE = 10 * 1024 * 1024 * 1024  # 10GB
MAX_PARTS_AMOUNT = 100
MAX_RETRIES = 3


class S3UploadFileService:
    """
    @autoapi False
    """

    def __init__(self, session, project_uid: str, workflow: str = "instant_containers"):
        self.session = session
        self.project_uid = project_uid
        self.workflow = workflow

    def upload_folder_into_s3(self, folder_path: str):
        """
        @autoapi False
        """

        self._validate_folder(folder_path)
        # TODO check if there is enough disk space before we start

        # zip the folder into a temp_dir and get the zip file path
        temp_dir = tempfile.mkdtemp()
        zip_file_path = self._zip_files_in_folder(temp_dir=temp_dir, folder_path=folder_path)
        file_size = zip_file_path.stat().st_size

        # calculate how to split the file into chunks and parts
        part_size, parts_amount, chunk_amount = self._calculate_part_size_and_chunk_amount(
            file_size
        )
        s3_folder = None
        create_chunk_parameters = {"workflow": self.workflow, "project_uid": self.project_uid}
        try:
            for chunk in range(0, chunk_amount):
                # calculate the part size and amount for the last chunk that cloud be a different size than the rest
                if chunk_amount > 1 and chunk == chunk_amount - 1:
                    part_size, parts_amount, _ = self._calculate_part_size_and_chunk_amount(
                        file_size % MAX_CHUNK_SIZE
                    )
                create_chunk_parameters["chunk_filename"] = f"chunk_number_{chunk}"
                upload_params = self.start_chunk_upload(create_chunk_parameters)
                # to connect the next call to the same upload we use the return folder
                create_chunk_parameters["folder"] = s3_folder = upload_params["folder"]
                try:
                    chunk_parts_upload_status = self.upload_chunk_to_s3(
                        part_size=part_size,
                        zip_file_path=zip_file_path,
                        chunk_num=chunk,
                        parts_amount=parts_amount,
                        upload_uid=upload_params["upload_uid"],
                        chunk_filepath=upload_params["chunk_filepath"],
                    )
                except Exception as e:
                    self.abort_upload(
                        upload_uid=upload_params["upload_uid"],
                        chunk_filepath=upload_params["chunk_filepath"],
                    )
                    raise Exception(
                        f"Failed to upload folder to S3. Aborting upload. support code: {upload_params['upload_uid']}"
                    )
                else:
                    self.mark_chunk_as_completed(
                        upload_uid=upload_params["upload_uid"],
                        chunk_filepath=upload_params["chunk_filepath"],
                        parts=chunk_parts_upload_status,
                    )
        finally:
            # remove the temp_dir
            shutil.rmtree(temp_dir)
        return s3_folder

    def start_chunk_upload(self, create_chunk_parameters: dict):
        response = self.session.post(
            "/multipart_upload/create",
            data=create_chunk_parameters,
            adapter_kwargs={"data_as_json": True},
        )
        if response.status_code == 200:
            return response.raw_response.json()
        else:
            raise Exception(f"Failed to start upload.")

    def upload_chunk_to_s3(
        self,
        part_size: int,
        zip_file_path: Path,
        chunk_num: int,
        parts_amount: int,
        upload_uid: str,
        chunk_filepath: str,
    ):
        parts_upload_data: Dict[str, Dict] = self._get_part_default_params(
            part_size=part_size,
            zip_file_path=zip_file_path,
            chunk_num=chunk_num,
            upload_uid=upload_uid,
            chunk_filepath=chunk_filepath,
            parts_amount=parts_amount,
        )
        s3_parts_status = []
        while not all([part["uploaded"] for part in parts_upload_data.values()]):
            results = []

            with ThreadPoolExecutor(os.cpu_count()) as executor:
                # execute tasks concurrently and process results in order
                for result in executor.map(
                    lambda params: self.upload_part(**params),
                    [part_params["params"] for part_id, part_params in parts_upload_data.items()],
                ):
                    # retrieve the result
                    results.append(result)
            for result in results:
                if result.get("error", None) is None:
                    parts_upload_data[result["part_id"]]["ETag"] = result["ETag"]
                    parts_upload_data[result["part_id"]]["ChecksumSHA256"] = result[
                        "ChecksumSHA256"
                    ]
                else:
                    parts_upload_data.pop(result["part_id"])
            s3_parts_status = self.get_s3_parts_status(upload_uid, chunk_filepath)
            if len(s3_parts_status) == 0:
                for part in parts_upload_data:
                    if parts_upload_data[part]["upload_attempt"] >= MAX_RETRIES:
                        raise Exception(f"Failed to data")
                    parts_upload_data[part]["upload_attempt"] += 1
            else:
                for part_status in s3_parts_status:
                    part_num = part_status["PartNumber"]
                    if self.was_part_uploaded_successfully(
                        parts_upload_data[part_num], part_status
                    ):
                        parts_upload_data[part_num]["uploaded"] = True
                    elif parts_upload_data[part_num]["upload_attempt"] < MAX_RETRIES:
                        parts_upload_data[part_num]["upload_attempt"] += 1
                    else:
                        # TODO: better error
                        raise Exception(f"Failed to data")
        response = [
            {"PartNumber": part["PartNumber"], "ETag": part["ETag"]} for part in s3_parts_status
        ]
        return response

    def get_s3_parts_status(self, upload_uid: str, chunk_filepath: str) -> list:
        """
        @autoapi False
        """
        parts_response = self.session.post(
            "/multipart_upload/uploaded_parts",
            data={
                "workflow": self.workflow,
                "project_uid": self.project_uid,
                "upload_uid": upload_uid,
                "chunk_filepath": chunk_filepath,
            },
            adapter_kwargs={"data_as_json": True},
        )
        if parts_response.status_code == 200:
            return parts_response.raw_response.json()["parts"]
        else:
            raise Exception(
                f"Failed to validate parts upload status: {parts_response.raw_response.text}"
            )

    def was_part_uploaded_successfully(self, part_validation_data: dict, part: dict) -> bool:
        """
        @autoapi False
        """
        return part["ETag"].strip('"') == part_validation_data["ETag"]

    def _validate_folder(self, folder_path: str) -> bool:
        """
        @autoapi False
        """
        if not Path(folder_path).is_dir():
            return False
        if Path(folder_path).stat().st_size == 0:
            return False
        return True

    def _zip_files_in_folder(self, temp_dir: str, folder_path: str) -> (Path, str):
        """
        @autoapi False
        """
        file_path = Path(temp_dir, "zipfile.zip")
        zf = zipfile.ZipFile(file_path, "w")
        path_str = Path(folder_path)
        for file in path_str.rglob("*"):
            if file.is_file():
                zf.write(file, str(file.relative_to(path_str)))
        zf.close()
        return Path(file_path)

    @staticmethod
    def _calculate_part_size_and_chunk_amount(file_size: int) -> (int, int, int):
        """
        Calculate how we should split the file based on its size and the S3 limits
        chunk_amount - how many 10GB chunks we should split the file to
        parts_amount - how many parts we should split each chunk to (between 1 and 100)
        part_size - the size of each part (between 5MB and 100MB)
        """
        # if file is bigger than 10GB, split it to multi chunks
        if file_size / MAX_CHUNK_SIZE > 1:
            chunk_amount = math.ceil(file_size / MAX_CHUNK_SIZE)
            part_size = MAX_PART_SIZE
            parts_amount = MAX_PARTS_AMOUNT
        else:
            chunk_amount = 1
            # S3 parts cant be smaller than 5MB and bigger than 100MB (the last part can be smaller than 5MB)
            part_size = max(math.ceil(file_size / MAX_PARTS_AMOUNT), MIN_PART_SIZE)
            parts_amount = math.ceil(file_size / part_size)
        return part_size, parts_amount, chunk_amount

    def mark_chunk_as_completed(self, upload_uid: str, chunk_filepath: str, parts: list):
        self.session.post(
            "/multipart_upload/complete",
            data={
                "workflow": self.workflow,
                "project_uid": self.project_uid,
                "upload_uid": upload_uid,
                "chunk_filepath": chunk_filepath,
                "parts": parts,
            },
            adapter_kwargs={"data_as_json": True},
        )

    def abort_upload(self, upload_uid: str, chunk_filepath: str):
        return self.session.post(
            "/multipart_upload/abort",
            data={
                "workflow": self.workflow,
                "project_uid": self.project_uid,
                "upload_uid": upload_uid,
                "chunk_filepath": chunk_filepath,
            },
            adapter_kwargs={"data_as_json": True},
        )

    def _get_part_default_params(
        self,
        part_size: int,
        zip_file_path: Path,
        chunk_num: int,
        upload_uid: str,
        chunk_filepath: str,
        parts_amount: int,
    ):
        # We are indexing the parts from 1, not from 0 to match the s3 id convention
        return {
            part_num: {
                "uploaded": False,
                "upload_attempt": 0,
                "ETag": "",
                "ChecksumSHA256": "",
                "params": {
                    "part_id": part_num,
                    "part_size": part_size,
                    "zip_file_path": zip_file_path,
                    "chunk_num": chunk_num,
                    "upload_uid": upload_uid,
                    "chunk_filepath": chunk_filepath,
                },
            }
            for part_num in range(1, parts_amount + 1)
        }

    def upload_part(
        self,
        part_id: int,
        zip_file_path: str,
        chunk_num: int,
        part_size: int,
        upload_uid: str,
        chunk_filepath: str,
    ):
        # go to the right position in the file
        with open(zip_file_path, "rb") as file_stream:
            # We are indexing the parts from 1, not from 0 to match the s3 id convention
            file_stream.seek((chunk_num * MAX_CHUNK_SIZE) + ((part_id - 1) * part_size))
            part_data: bytes = file_stream.read(part_size)
            if part_data:
                # calculate the ETag and ChecksumSHA256 for the part data to use in validation
                etag = self._calculate_etag(part_data)
                checksum = self._calculate_checksum(part_data)
                # start a async task to upload the part
                self.make_upload_part_request(
                    part_id=part_id,
                    upload_uid=upload_uid,
                    chunk_filepath=chunk_filepath,
                    part_data=part_data,
                    checksum=checksum,
                )
                return {"part_id": part_id, "ETag": etag, "ChecksumSHA256": checksum}
            else:
                return {"part_id": part_id, "error": "part_data is empty"}

    def make_upload_part_request(
        self, part_id: int, upload_uid: str, chunk_filepath: str, part_data: bytes, checksum: str
    ):
        """
        @autoapi False
        """
        part_response = self.session.post(
            "/multipart_upload/request_part_url",
            data={
                "workflow": self.workflow,
                "project_uid": self.project_uid,
                "part_id": part_id,
                "upload_uid": upload_uid,
                "chunk_filepath": chunk_filepath,
                # TODO - add checksum_sha_256
                # "checksum_sha_256": str(checksum),
                "part_size": len(part_data),
            },
            adapter_kwargs={"data_as_json": True},
        )
        self.upload_part_to_s3(
            url=part_response.raw_response.json()["url"],
            part_data=part_data,
            checksum=str(checksum),
        )

    def upload_part_to_s3(self, url: str, part_data: bytes, checksum: str):
        """
        @autoapi False
        """
        requests.put(
            url,
            data=part_data,
            headers={
                "Content-Length": str(len(part_data)),
                # "Content-SHA256": checksum,
                "ContentType": "application/zip",
            },
        )

    def _calculate_etag(self, part_data: bytes) -> str:
        """
        @autoapi False
        """
        return hashlib.md5(part_data).hexdigest()

    def _calculate_checksum(self, part_data: bytes) -> str:
        """
        @autoapi False
        """
        return base64.b64encode(hashlib.sha256(part_data).digest()).decode("ascii")
