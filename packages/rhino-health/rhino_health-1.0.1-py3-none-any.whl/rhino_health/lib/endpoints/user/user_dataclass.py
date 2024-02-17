from enum import Enum
from typing import Any, List, Optional

from pydantic import Field
from typing_extensions import Annotated

from rhino_health.lib.dataclass import RhinoBaseModel


class UserWorkgroupRole(str, Enum):
    MEMBER = "Member"
    WORKGROUP_ADMIN = "Workgroup Admin"
    ORG_ADMIN = "Org Admin"
    RHINO_ADMIN = "Rhino Admin"

    @classmethod
    def is_admin_member(cls, member_role) -> bool:
        return member_role in {cls.WORKGROUP_ADMIN, cls.ORG_ADMIN, cls.RHINO_ADMIN}

    @classmethod
    def is_non_admin_member(cls, member_role, is_primary_workgroup=False) -> bool:
        if is_primary_workgroup:
            return member_role in {None, cls.MEMBER}
        return member_role in {cls.MEMBER}


class LTSUser(RhinoBaseModel):
    """
    @autoapi False
    """

    uid: str
    """@autoapi True Unique ID of the user"""
    full_name: str
    """@autoapi True The full name of the user"""
    primary_workgroup_uid: Annotated[str, Field(alias="primary_workgroup")]
    """@autoapi True The Unique ID of the Primary Workgroup of the user"""
    workgroups_uids: Annotated[List[str], Field(alias="workgroups")]
    """@autoapi True Additional workgroup unique IDs the user belongs to"""
    primary_workgroup_role: Optional[UserWorkgroupRole] = UserWorkgroupRole.MEMBER
    """@autoapi True Elevated roles the user has in their primary workgroup."""

    # API responses we do not want to surface to the user
    __hidden__ = ["first_name", "profile_pic", "otp_enabled"]


class User(LTSUser):
    """
    @objname User
    DataClass representing a User on the Rhino platform.
    """

    _primary_workgroup: Any = None
    _workgroups: Any = None

    @property
    def primary_workgroup(self):
        """
        Return the primary workgroup associated with this User

        .. warning:: The result of this function is cached.
            Be careful calling this function after making changes to the user

        Returns
        -------
        primary_workgroup: Workgroup
            DataClass representing the Primary Workgroup of the User
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
    def workgroups(self):
        """
        Get the additional Workgroups of this User

        .. warning:: Be careful when calling this for newly created objects.
            The workgroups associated with the WORKGROUP_UIDS must already exist on the platform.

        .. warning:: The result of this function is cached.
            Be careful calling this function after making changes to the user

        Returns
        -------
        workgroups: List[Workgroup]
            A List of DataClasses representing the Workgroups this user belongs to

        See Also
        --------
        rhino_health.lib.endpoints.workgroup.workgroup_dataclass : Workgroup Dataclass
        """
        if self._workgroups:
            return self._workgroups
        if self.workgroups_uids:
            self._workgroups = self.session.workgroup.get_workgroups(self.workgroups_uids)
            return self._workgroups
        else:
            return []
