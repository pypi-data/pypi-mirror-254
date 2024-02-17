from typing import Any, Dict, List, Optional

from pydantic import Field
from typing_extensions import Annotated, Literal

from rhino_health.lib.dataclass import RhinoBaseModel
from rhino_health.lib.endpoints.endpoint import VersionMode
from rhino_health.lib.endpoints.user.user_dataclass import LTSUser, User
from rhino_health.lib.utils import alias


class ProjectCreateInput(RhinoBaseModel):
    """
    Input arguments for adding a new project.
    """

    name: str
    """@autoapi True The name of the Project"""
    description: str
    """@autoapi True The description of the Project"""
    type: Literal["Validation", "Refinement"]
    """@autoapi True The type of the Project"""
    primary_workgroup_uid: Annotated[str, Field(alias="primary_workgroup")]
    """@autoapi True The unique ID of the Project's Primary Workgroup"""
    permissions: Optional[str] = None
    """@autoapi True JSON-encoded project-level permissions"""


class LTSProject(ProjectCreateInput):
    """
    @autoapi False

    A Project that exists on the Rhino Health Platform
    """

    uid: str
    """@autoapi True The unique ID of the Project"""
    slack_channel: str
    """@autoapi True Slack Channel URL for communications for the Project"""
    collaborating_workgroup_uids: Annotated[List[str], Field(alias="collaborating_workgroups")]
    """@autoapi True A list of unique IDs of the Project's collaborating Workgroups"""


class Project(LTSProject):
    """
    @objname Project
    DataClass representing a Project on the Rhino platform.
    """

    _users: Optional[List[User]] = None
    _collaborating_workgroups: Any = None
    _primary_workgroup: Any = None
    created_at: str
    creator_uid: Annotated[str, Field(alias="creator")]
    _creator: Any = None
    """@autoapi True When this Project was added"""

    @property
    def creator(self):
        """
        @autoapi True

        Get the User who created the Project

        .. warning:: Be careful when calling this for newly created objects.
            The user associated with the CREATOR_UID must already exist on the platform.

        .. warning:: The result of this function is cached.
            Be careful calling this function after making changes to the Project.

        Returns
        -------
        user: User
            The User who created the Project

        See Also
        --------
        rhino_health.lib.endpoints.user.user_dataclass : User Dataclass
        """

        if self._creator is not None:
            return self._creator
        self._creator = self.session.user.get_users([self.creator_uid])[0]
        return self._creator

    @property
    def stats(self):
        """
        Returns metadata for this project
        """
        return self.session.project.get_project_stats(self.uid)

    @property
    def status(self):
        """
        @autoapi False
        """
        return alias(
            self.stats,
            old_function_name="status",
            new_function_name="stats",
            base_object="Project",
            is_property=True,
        )()

    @property
    def primary_workgroup(self):
        """
        Return the primary workgroup associated with this Project

        Returns
        -------
        primary_workgroup: Workgroup
            DataClasses representing the Primary Workgroup of the Project
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

    @property
    def collaborating_workgroups(self):
        """
        Get the Collaborating Workgroup DataClass of this Project

        .. warning:: Be careful when calling this for newly created objects.
            The workgroups associated with the COLLABORATING_WORKGROUP_UIDS must already exist on the platform.

        .. warning:: The result of this function is cached.
            Be careful calling this function after making changes to the collaborating workgroups

        Returns
        -------
        collaborating_workgroups: List[Workgroup]
            A List of DataClasses representing the Collaborating Workgroups of the Project

        See Also
        --------
        rhino_health.lib.endpoints.workgroup.workgroup_dataclass : Workgroup Dataclass
        """
        if self._collaborating_workgroups:
            return self._collaborating_workgroups
        if self.collaborating_workgroup_uids:
            self._collaborating_workgroups = self.session.project.get_collaborating_workgroups(self)
            return self._collaborating_workgroups
        else:
            return []

    def add_collaborator(self, collaborator_or_uid):
        """
        Adds COLLABORATOR_OR_UID as a collaborator to this project

        .. warning:: This feature is under development and the interface may change
        """
        from ..workgroup.workgroup_dataclass import LTSWorkgroup

        if isinstance(collaborator_or_uid, LTSWorkgroup):
            collaborator_or_uid = collaborator_or_uid.uid
        self.session.project.add_collaborator(
            project_uid=self.uid, collaborating_workgroup_uid=collaborator_or_uid
        )
        self._collaborating_workgroups = None
        self.collaborating_workgroup_uids.append(collaborator_or_uid)
        return self

    def remove_collaborator(self, collaborator_or_uid):
        """
        Removes COLLABORATOR_OR_UID as a collaborator from this project

        .. warning:: This feature is under development and the interface may change
        """
        from ..workgroup.workgroup_dataclass import LTSWorkgroup

        if isinstance(collaborator_or_uid, LTSWorkgroup):
            collaborator_or_uid = collaborator_or_uid.uid
        self.session.project.remove_collaborator(
            project_uid=self.uid, collaborating_workgroup_uid=collaborator_or_uid
        )
        self._collaborating_workgroups = None
        self.collaborating_workgroup_uids.remove(collaborator_or_uid)
        return self

    @property
    def datasets(self):
        """
        Get Datasets associated with this project

        See Also
        --------
        rhino_health.lib.endpoints.project.project_endpoints.ProjectEndpoints.get_datasets : Full documentation
        """
        return self.session.project.get_datasets(self.uid)

    def get_dataset_by_name(self, name, version=VersionMode.LATEST, **_kwargs):
        """
        Get Dataset associated with this project

        See Also
        --------
        rhino_health.lib.endpoints.project.project_endpoints.ProjectEndpoints.get_dataset_by_name : Full documentation
        """
        return self.session.project.get_dataset_by_name(name, project_uid=self.uid, version=version)

    def search_for_datasets_by_name(
        self, name, version=VersionMode.LATEST, name_filter_mode=None, **_kwargs
    ):
        """
        Get Datasets associated with this project

        See Also
        --------
        rhino_health.lib.endpoints.project.project_endpoints.ProjectEndpoints.search_for_datasets_by_name : Full documentation
        """
        return self.session.project.search_for_datasets_by_name(
            name, project_uid=self.uid, version=version, name_filter_mode=name_filter_mode
        )

    @property
    def data_schemas(self):
        """
        Get Data Schemas associated with this project

        See Also
        --------
        rhino_health.lib.endpoints.project.project_endpoints.ProjectEndpoints.get_data_schemas : Full documentation
        """
        return self.session.project.get_data_schemas(self.uid)

    def get_data_schema_by_name(self, name, version=VersionMode.LATEST, **_kwargs):
        """
        Get DataSchema associated with this project

        See Also
        --------
        rhino_health.lib.endpoints.project.project_endpoints.ProjectEndpoints.get_data_schema_by_name : Full documentation
        """
        return self.session.project.get_data_schema_by_name(
            name, project_uid=self.uid, version=version
        )

    def search_for_data_schemas_by_name(
        self, name, version=VersionMode.LATEST, name_filter_mode=None, **_kwargs
    ):
        """
        Get Data Schemas associated with this project

        See Also
        --------
        rhino_health.lib.endpoints.project.project_endpoints.ProjectEndpoints.search_for_data_schemas_by_name : Full documentation
        """
        return self.session.project.search_for_data_schemas_by_name(
            name, project_uid=self.uid, version=version, name_filter_mode=name_filter_mode
        )

    @property
    def code_objects(self):
        """
        Get CodeObjects associated with this project

        See Also
        --------
        rhino_health.lib.endpoints.project.project_endpoints.ProjectEndpoints.get_code_objects : Full documentation
        """
        return self.session.project.get_code_objects(self.uid)

    def get_code_object_by_name(self, name, version=VersionMode.LATEST, **_kwargs):
        """
        Get CodeObject associated with this project

        See Also
        --------
        rhino_health.lib.endpoints.project.project_endpoints.ProjectEndpoints.get_code_object_by_name : Full documentation
        """
        return self.session.project.get_code_object_by_name(
            name, project_uid=self.uid, version=version
        )

    def search_for_code_objects_by_name(
        self, name, version=VersionMode.LATEST, name_filter_mode=None, **_kwargs
    ):
        """
        Get CodeObjects associated with this project

        See Also
        --------
        rhino_health.lib.endpoints.project.project_endpoints.ProjectEndpoints.search_for_code_objects_by_name : Full documentation
        """
        return self.session.project.search_for_code_objects_by_name(
            name, project_uid=self.uid, version=version, name_filter_mode=name_filter_mode
        )

    @property
    def users(self):
        """
        Return users of this project
        """
        if self._users is None:
            self._users = self.session.user._search_for_users_by_name(name="", project_uid=self.uid)
        return self._users

    def aggregate_dataset_metric(self, *args, **kwargs):
        """
        Performs an aggregate dataset metric

        See Also
        --------
        rhino_health.lib.endpoints.project.project_endpoints.ProjectEndpoints.aggregate_dataset_metric : Full documentation
        """
        return self.session.project.aggregate_dataset_metric(*args, **kwargs)

    def joined_dataset_metric(self, *args, **kwargs):
        """
        Performs a federated join dataset metric

        See Also
        --------
        rhino_health.lib.endpoints.project.project_endpoints.ProjectEndpoints.joined_dataset_metric : Full documentation
        """
        return self.session.project.joined_dataset_metric(*args, **kwargs)

    # Add Schema
    # Local Schema from CSV

    def get_agent_resources_for_workgroup(self, *args, **kwargs):
        return self.session.project.get_system_resources_for_workgroup(*args, **kwargs)


class SystemResources(RhinoBaseModel):
    """
    Output when calling system resources.
    """

    filesystem_storage: dict
    """@autoapi True filesystem storage in bytes (free, used, total)"""
    cpu_percent_used: float
    """@autoapi True used cpu percent"""
    memory: dict
    """@autoapi True Memory data in bytes (free, used, total)"""
    gpu: dict
    """@autoapi True The GPU usage data per gpu"""
