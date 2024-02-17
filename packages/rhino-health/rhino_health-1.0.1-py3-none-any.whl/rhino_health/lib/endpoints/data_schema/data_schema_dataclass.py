import csv
from typing import Any, Dict, List, Optional
from warnings import warn

from pydantic import BaseModel, Field, RootModel
from typing_extensions import Annotated

from rhino_health.lib.dataclass import RhinoBaseModel


class SchemaField(BaseModel):
    """
    A schema field
    """

    # TODO: Better type checks
    name: str
    identifier: Optional[str] = None
    description: Optional[str] = None
    role: Optional[str] = None
    type: Optional[str] = None
    type_params: Any = None
    units: Optional[str] = None
    may_contain_phi: Optional[bool] = None
    permissions: Optional[str] = None


class SchemaFields(RootModel):
    """
    List-like dataclass that provides some convenience functions
    Pydantic v2 uses RootModel to handle internal things required for serialization
    """

    root: List[Any]  # The actual type

    def __init__(self, schema_fields: List[Dict]):
        schema_fields = self._parse_data(schema_fields)
        super(SchemaFields, self).__init__(schema_fields)

    def __iter__(self):
        for schema_field in self.root:
            yield schema_field

    @property
    def field_names(self):
        return [variable.name for variable in self.root]

    def _parse_data(self, schema_fields: List[Dict]):
        return [SchemaField(**schema_field) for schema_field in schema_fields]

    def dict(self, *args, **kwargs):
        return [schema_field.dict(*args, **kwargs) for schema_field in self]

    def to_csv(self, output_file):
        """
        @autoai False
        """
        # TODO: RH-1871 Ability to write to CSV again
        raise NotImplementedError


class BaseDataSchema(RhinoBaseModel):
    """
    @autoapi False
    Base DataSchema used by both return result and creation
    """

    name: str
    """@autoapi True The name of the DataSchema"""
    description: str
    """@autoapi True The description of the DataSchema"""
    base_version_uid: Optional[str] = None
    """@autoapi True If this DataSchema is a new version of another DataSchema, the original Unique ID of the base DataSchema."""
    primary_workgroup_uid: Annotated[str, Field(alias="primary_workgroup")]
    """@autoapi True The UID of the primary workgroup for this data schema"""
    version: Optional[int] = 0
    """@autoapi True The revision of this DataSchema"""
    project_uids: Annotated[List[str], Field(alias="projects")]
    """@autoapi True A list of UIDs of the projects this data schema is associated with"""


class DataSchemaCreateInput(BaseDataSchema):
    """
    @autoapi True
    Input for creating a new DataSchema

    Examples
    --------
    >>> DataSchemaCreateInput(
    >>>     name="My DataSchema",
    >>>     description="A Sample DataSchema",
    >>>     primary_workgroup_uid=project.primary_workgroup_uid,
    >>>     projects=[project.uid],
    >>>     file_path="/absolute/path/to/my_schema_file.csv"
    >>> )
    """

    schema_fields: List[str] = []
    """ A list of rows representing the schema fields from a csv file.

    Users are recommended to use file_path instead of directly setting this value
    
    The first row should be the field names in the schema. Each list string should have a newline at the end.
    Each row should have columns separated by commas.
    """
    file_path: Optional[str] = None
    """ Path to a `CSV <https://en.wikipedia.org/wiki/Comma-separated_values>`_ File 
    that can be opened with python's built in `open() <https://docs.python.org/3/library/functions.html#open>`_ command.
    """

    def __init__(self, **data):
        self._load_csv_file(data)
        super(BaseDataSchema, self).__init__(**data)

    def _load_csv_file(self, data):
        file_path = data.get("file_path", None)
        if file_path:
            data["schema_fields"] = [
                x for x in open(file_path, "r", encoding="utf-8", newline=None).readlines()
            ]
            # TODO: Verify the schema file is correct
            del data["file_path"]


class LTSDataSchema(BaseDataSchema):
    """
    @autoapi False
    """

    uid: Optional[str] = None
    """@autoapi True The Unique ID of the DataSchema"""
    created_at: str
    """@autoapi True When this DataSchema was created"""


class DataSchema(LTSDataSchema):
    """
    @autoapi True

    A DataSchema in the system used by Datasets
    """

    schema_fields: SchemaFields
    """@autoapi True A list of schema fields in this data schema"""
    _projects: Any = None
    _primary_workgroup: Any = None
    _creator: Any = None
    creator_uid: Annotated[str, Field(alias="creator")]

    """
    Who created this DataSchema
    """

    def __init__(self, **data):
        self._handle_schema_fields(data)
        super().__init__(**data)

    def _handle_schema_fields(self, data):
        raw_schema_field = data["schema_fields"]
        data["schema_fields"] = SchemaFields(raw_schema_field)

    @property
    def creator(self):
        """
        @autoapi True

        Get the User who created the DataSchema

        .. warning:: Be careful when calling this for newly created objects.
            The user associated with the CREATOR_UID must already exist on the platform.

        .. warning:: The result of this function is cached.
            Be careful calling this function after making changes to the DataSchema.

        Returns
        -------
        user: User
            The User who created the DataSchema

        See Also
        --------
        rhino_health.lib.endpoints.user.user_dataclass : User Dataclass
        """

        if self._creator is not None:
            return self._creator
        self._creator = self.session.user.get_users([self.creator_uid])[0]
        return self._creator

    @property
    def projects(self):
        """
        @autoapi True

        Get the projects of using this DataSchema

        .. warning:: Be careful when calling this for newly created objects.
            The projects associated with the PROJECT_UIDS must already exist on the platform.

        .. warning:: The result of this function is cached.
            Be careful calling this function after making changes to the DataSchema

        Returns
        -------
        projects: List[Project]
            A DataClass representing the Project of the user's primary workgroup

        See Also
        --------
        rhino_health.lib.endpoints.project.project_dataclass : Project Dataclass
        """
        if self._projects:
            return self._projects
        if self.project_uids:
            self._projects = self.session.project.get_projects(self.project_uids)
            return self._projects
        else:
            return None

    def delete(self):
        if not self._persisted or not self.uid:
            raise RuntimeError("DataSchema has already been deleted")

        self.session.data_schema.remove_data_schema(self.uid)
        self._persisted = False
        self.uid = None
        return self

    @property
    def primary_workgroup(self):
        """
        Return the primary workgroup associated with this DataSchema

        .. warning:: The result of this function is cached.
            Be careful calling this function after making changes to the project

        Returns
        -------
        primary_workgroup: Workgroup
            DataClasses representing the Primary Workgroup of the DataSchema
        """
        if self._primary_workgroup:
            return self._primary_workgroup
        if self.primary_workgroup_uid:
            self._primary_workgroup = self.session.workgroup.get_workgroups(
                [self.primary_workgroup_uid]
            )[0]
            return self._primary_workgroup
        else:
            return None


from rhino_health.lib.endpoints.user.user_dataclass import LTSUser

LTSDataSchema.model_rebuild()
DataSchema.model_rebuild()
