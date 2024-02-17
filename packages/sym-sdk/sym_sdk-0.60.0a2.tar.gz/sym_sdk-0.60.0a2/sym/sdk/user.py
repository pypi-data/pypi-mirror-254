"""Representations of Users in both Sym and third parties."""

import itertools
from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Dict, List, Literal, Optional, Set
from uuid import UUID

from sym.sdk.request_permission import PermissionLevel

from .resource import SymBaseResource

if TYPE_CHECKING:
    from sym.sdk.templates import approval


def user_ids(user_list: List["User"]) -> List[UUID]:
    """Fetch a list of User IDs from a list of Users."""
    return [user.id for user in user_list]


class UserIdentity(ABC, SymBaseResource):
    """Represents a :class:`~sym.sdk.user.User`'s
    identity in an external system such as Slack or PagerDuty.
    """

    def __str__(self) -> str:
        return f"Identity({self.service}: {self.user_id})"

    def __repr__(self) -> str:
        return str(self)

    @property
    @abstractmethod
    def service(self) -> str:
        """The name of the external system providing the identity.

        For example, :mod:`~sym.sdk.integrations.slack`.
        """

    @property
    @abstractmethod
    def service_id(self) -> str:
        """The ID of the external system providing the identity.

        For example, "T123ABC" for a Slack Workspace.
        """

    @property
    @abstractmethod
    def user_id(self) -> str:
        """The :class:`~sym.sdk.user.User`'s identifier in the external system.

        For example, the :class:`~sym.sdk.user.User`'s Slack ID.
        """


class UserRole(str, Enum):
    """UserRoles represent very basic permission sets for users in the Sym platform.

    UserRoles are defined in descending order of permissions. Each role should include
    all permissions of the roles below it.
    """

    ADMIN = "admin"
    """Admins are allowed to do anything.
    (e.g. Use symflow CLI, run Flows, apply Terraform)
    """

    MEMBER = "member"
    """Members can run Flows and interact with requests."""

    GUEST = "guest"
    """Guests can approve/deny/revoke requests, if the Flow is configured to allow guest interactions"""

    def permission_levels(self) -> Set[PermissionLevel]:
        """Returns a set of PermissionLevels that apply to the role."""
        if self == self.ADMIN:
            return {PermissionLevel.ADMIN, PermissionLevel.MEMBER, PermissionLevel.ALL_USERS}
        elif self == self.MEMBER:
            return {PermissionLevel.MEMBER, PermissionLevel.ALL_USERS}
        else:
            return {PermissionLevel.ALL_USERS}


class User(ABC, SymBaseResource):
    """The atomic representation of a user in Sym.

    :class:`~sym.sdk.user.User`s have many :class:`~sym.sdk.user.UserIdentity`,
    which are used for referencing said user in external systems.
    """

    def __str__(self) -> str:
        identities = list(itertools.chain.from_iterable(self.identities.values()))
        return f"User(email={self.email}, username={self.username}, identities={identities})"

    def __repr__(self) -> str:
        return f"User({self.username})"

    def __hash__(self):
        return hash(self.__class__) + hash(self.username)

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.username == other.username

    @property
    @abstractmethod
    def id(self) -> UUID:
        """The :class:`~sym.sdk.user.User`'s globally unique identifier."""

    @property
    @abstractmethod
    def email(self) -> Optional[str]:
        """The :class:`~sym.sdk.user.User`'s email if the user is of type "normal", or None otherwise."""

    @property
    @abstractmethod
    def username(self) -> str:
        """The :class:`~sym.sdk.user.User`'s username if the user is of type "bot", or
        the email if the user is of type "normal".
        """

    @property
    @abstractmethod
    def type(self) -> str:
        """The :class:`~sym.sdk.user.User`'s type (i.e., "bot" or "normal")."""

    @property
    @abstractmethod
    def first_name(self) -> Optional[str]:
        """The :class:`~sym.sdk.user.User`'s first name."""

    @property
    @abstractmethod
    def last_name(self) -> Optional[str]:
        """The :class:`~sym.sdk.user.User`'s last name."""

    @property
    @abstractmethod
    def identities(self) -> Dict[str, List[UserIdentity]]:
        """Retrieves the set of identities associated with this
        :class:`~sym.sdk.user.User`, grouped by service type.

        A mapping of service types to lists of :class:`~sym.sdk.user.UserIdentity`.
        """

    @property
    @abstractmethod
    def role(self) -> UserRole:
        """The :class:`~sym.sdk.user.User`'s role (i.e., "admin", "member", or "guest")."""

    @abstractmethod
    def identity(
        self,
        service_type: str,
        service_id: Optional[str] = None,
    ) -> Optional[UserIdentity]:
        """Retrieves this :class:`~sym.sdk.user.User`'s :class:`~sym.sdk.user.UserIdentity`
        for a particular external system.

        External systems specified by a service_type, and optionally a service_id.

        Args:
            service_type: The name of one of Sym's :mod:`~sym.sdk.integrations`.
            service_id: An identifier for an instance of a service, such as a Slack Workspace ID.

        Returns:
            A :class:`~sym.sdk.user.UserIdentity`, or None if no identity is found for the Integration.
        """

    @abstractmethod
    def get_event_count(
        self,
        event_name: "approval.ApprovalTemplateStep",
        since: Optional[datetime] = None,
        until: Optional[datetime] = None,
        filter_on: Literal["flow", "target"] = "flow",
        include_errored: bool = False,
    ) -> int:
        """Retrieve a count of :class:`Events <sym.sdk.event.Event>` that have occurred on
        :class:`Runs <sym.sdk.flow.Run>` where this :class:`~sym.sdk.user.User` was the requester.

        For example, to determine whether this :class:`~sym.sdk.user.User` has ever been granted
        access to the current :class:`~sym.sdk.flow.Flow` via Sym, the following check could be
        used::

            if user.get_event_count(
                event_name=ApprovalTemplateStep.ESCALATE,
                filter_on="flow",
            ) > 0:
                ...

        Args:
            event_name: The name of the :class:`~sym.sdk.event.Event` to count.
            since: Filter counted :class:`Events <sym.sdk.event.Event>` to those that were scheduled
                to be processed at or after this time.
            until: Filter counted :class:`Events <sym.sdk.event.Event>` to those that were scheduled
                to be processed at or before this time.
            filter_on: Filter counted :class:`Events <sym.sdk.event.Event>` to those that occurred
                on :class:`Runs <sym.sdk.flow.Run>` using the same :class:`~sym.sdk.flow.Flow` if
                "flow" is given, or where the same :class:`~sym.sdk.target.AccessTarget` was
                requested if "target" is given.
            include_errored: Whether to count :class:`Events <sym.sdk.event.Event>` that were
                ignored or encountered errors while being processed.
        """
