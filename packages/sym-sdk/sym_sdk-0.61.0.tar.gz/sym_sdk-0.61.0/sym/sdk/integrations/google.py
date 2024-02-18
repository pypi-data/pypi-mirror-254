"""Helpers for interacting with Google APIs within the Sym SDK."""

from typing import List, Optional

from sym.sdk.exceptions import GoogleError  # noqa
from sym.sdk.user import User


def is_user_in_group(user: User, *, group_email: str) -> bool:
    """Checks if the provided user is a member of the specified Google Group.
    Membership may either be direct or indirect.

    **Prerequisites**:

    - To call this method, your ``gcp_connector`` module must have ``enable_google_group_management = true``.

    Args:
        user: The User to check
        group_email: The email identifier of the Google Group

    Returns:
        True if the user is part of the Google Group
    """


def list_groups(domain: Optional[str] = None) -> List[dict]:
    """Returns a list of all groups for the Google Workspace account or given domain.

    Args:
        domain: An optional domain to only get groups from the given domain (e.g. a secondary domain).
            If not provided, this method will retrieve all groups associated with all domains for this Google
            Workspace account.

    Returns:
        A list of dictionaries, with each dictionary representing a Google Group.
        See Google's docs for the dictionary structure: https://developers.google.com/admin-sdk/directory/reference/rest/v1/groups#Group
    """


def users_in_group(group_email: str, *, include_indirect_members: bool = True) -> List[User]:
    """Returns a list of users in the specified Google Group.

    Note that this method only returns emails corresponding to User accounts. If the specified Google Group contains
    nested Google Groups, those group emails will not be included in the returned list.

    Args:
        group_email: The email identifier of the Google Group.
        include_indirect_members: Whether to include users who are indirect members of the given group.
            Defaults to True.

    Returns:
        A List of User objects
    """
