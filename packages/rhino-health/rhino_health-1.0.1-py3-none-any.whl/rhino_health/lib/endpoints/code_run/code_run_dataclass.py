import itertools
from enum import Enum
from typing import Any, Dict, List, Optional

import arrow
from funcy import flatten
from pydantic import Field
from typing_extensions import Annotated

from rhino_health.lib.dataclass import RhinoBaseModel


class CodeRunStatus(str, Enum):
    INITIALIZING = "Initializing"
    STARTED = "Started"
    COMPLETED = "Completed"
    FAILED = "Failed"
    HALTING = "Halting"
    HALTED_SUCCESS = "Halted: Success"
    HALTED_FAILURE = "Halted: Failure"  # Indicating the halting action failed


class CodeRun(RhinoBaseModel):
    uid: str
    """The unique ID of the CodeRun"""
    action_type: str
    """The type of action preformed"""
    status: CodeRunStatus
    """The action status"""
    start_time: str
    """The action start time"""
    end_time: Any = None
    """The action end time"""
    _code_object: Any = None
    _input_datasets: Any = None
    _output_datasets: Any = None
    input_dataset_uids: Optional[List[List[str]]] = None
    """
    A list of dataset uids. Each entry is a list of datasets corresponding to a data_schema on the CodeObject
    [[first_dataset_for_first_run, second_dataset_for_first_run ...], [first_dataset_for_second_run, second_dataset_for_second_run ...], ...]
    """
    output_dataset_uids: Optional[List[List[str]]] = None
    """
    A list of dataset uids. Each entry is a list of of datasets corresponding to a data_schema on the CodeObject
    [[first_dataset_for_first_run, second_dataset_for_first_run ...], [first_dataset_for_second_run, second_dataset_for_second_run ...], ...]
    """
    code_object_uid: Annotated[str, Field(alias="code_object")]
    """The relevant code_object object"""
    results_info: Optional[Dict[str, Any]] = None
    """The run result info"""
    results_report: Optional[str] = None
    """The run result report"""
    report_images: List[Any]
    """The run result images"""
    # Note pydantic fields cannot start with model
    paths_to_model_params: Annotated[
        Optional[List[str]], Field(alias="model_params_external_storage_paths")
    ] = None
    """The external paths where model param results are stored, if any"""
    _creator: Any = None
    creator_uid: Annotated[str, Field(alias="creator")]
    """Who ran this code"""

    # API responses we do not want to surface to the user
    __hidden__ = [
        "config_info",  # Internal Task UID data
        "input_sal_uids",  # Internal usage no SAL object in SDK
        "igc_ui_access_url",  # Not for SDK
    ]

    @property
    def creator(self):
        """
        @autoapi True

        Get the User who created the CodeRun

        .. warning:: The result of this function is cached.
            Be careful calling this function after making changes to the CodeRun

        Returns
        -------
        user: User
            The User who created the CodeRun

        See Also
        --------
        rhino_health.lib.endpoints.user.user_dataclass : User Dataclass
        """

        if self._creator is not None:
            return self._creator
        self._creator = self.session.user.get_users([self.creator_uid])[0]
        return self._creator

    @property
    def code_object(self):
        """
        @autoapi True
        Return the CodeObject associated with this CodeRun

        .. warning:: The result of this function is cached.
            Be careful calling this function after making changes

        Returns
        -------
        code_object: CodeObject
            DataClasses representing the CodeObject
        """
        if self._code_object:
            return self._code_object
        if self.code_object_uid:
            self._code_object = self.session.code_object.get_code_object(self.code_object_uid)
            return self._code_object
        else:
            return None

    @property
    def input_datasets(self):
        """
        @autoapi True
        Return the Input Datasets that were used for this CodeRun

        .. warning:: The result of this function is cached.
            Be careful calling this function after making changes

        Returns
        -------
        datasets: List[Dataset]
            DataClasses representing the Datasets
        """
        if self._input_datasets:
            return self._input_datasets
        results = []
        for dataset_uid in list(flatten(self.input_dataset_uids)):
            results.append(self.session.dataset.get_dataset(dataset_uid))
        self._input_datasets = results
        return results

    @property
    def output_datasets(self):
        """
        @autoapi True
        Return the Output Datasets that were used for this CodeRun

        .. warning:: The result of this function is cached.
            Be careful calling this function after making changes

        Returns
        -------
        datasets: List[Dataset]
            DataClasses representing the Datasets
        """
        if self._output_datasets:
            return self._output_datasets
        results = []
        for dataset_uid in list(flatten(self.output_dataset_uids)):
            results.append(self.session.dataset.get_dataset(dataset_uid))
        self._output_datasets = results
        return results

    def save_model_params(self, file_name):
        """
        Saves the model params to a file.

        .. warning:: This feature is under development and the interface may change

        Parameters
        ----------
        file_name: str
            Name of the file to save to
        """
        model_params = self.session.code_run.get_model_params()
        with open(file_name, "wb") as output_file:
            output_file.write(model_params.getbuffer())

    @property
    def _process_finished(self):
        """
        @autoapi False
        """
        return self.status in {
            CodeRunStatus.COMPLETED,
            CodeRunStatus.FAILED,
            CodeRunStatus.HALTED_SUCCESS,
            CodeRunStatus.HALTED_FAILURE,
        }

    def wait_for_completion(
        self, timeout_seconds: int = 500, poll_frequency: int = 10, print_progress: bool = True
    ):
        """
        @autoapi True
        Wait for the asynchronous CodeRun to complete

        Parameters
        ----------
        timeout_seconds: int = 500
            How many seconds to wait before timing out
        poll_frequency: int = 10
            How frequent to check the status, in seconds
        print_progress: bool = True
            Whether to print how long has elapsed since the start of the wait

        Returns
        -------
        code_run: CodeRun
            DataClass representing the CodeRun of the run

        See Also
        --------
        rhino_health.lib.endpoints.code_run.code_run_dataclass.CodeRun: Response object
        """
        return self._wait_for_completion(
            name="code run",
            is_complete=self._process_finished,
            query_function=lambda code_run: code_run.session.code_run.get_code_run(code_run.uid),
            validation_function=lambda old, new: (new.status and new._process_finished),
            timeout_seconds=timeout_seconds,
            poll_frequency=poll_frequency,
            print_progress=print_progress,
        )

    # def __logs(self):
    #     return self.session.code_run.__logs(self.uid)

    @property
    def warnings(self):
        """
        Returns any warnings that occurred during this run
        """
        tasks_errors_and_warnings = self.results_info.get("tasks_errors_and_warnings") or []
        warnings = self.results_info.get("warnings") or []
        warnings += list(
            itertools.chain.from_iterable(
                [x.get("warnings") or [] for x in tasks_errors_and_warnings]
            )
        )
        return warnings

    @property
    def errors(self):
        """
        Returns any errors that occurred during this run
        """
        tasks_errors_and_warnings = self.results_info.get("tasks_errors_and_warnings") or []
        errors = self.results_info.get("errors") or []
        errors += list(
            itertools.chain.from_iterable(
                [x.get("errors") or [] for x in tasks_errors_and_warnings]
            )
        )
        return errors
