"""Helpers for interacting with a Slack workspace."""

from typing import List, Optional, Sequence, Union

from sym.sdk.exceptions.slack import SlackError  # noqa
from sym.sdk.request_destination import (
    RequestDestination,
    RequestDestinationFallback,
    SlackChannelID,
    SlackChannelName,
    SlackUser,
    SlackUserGroup,
)
from sym.sdk.user import User


def user(
    identifier: Union[str, User], allow_self: bool = False, timeout: Optional[int] = None
) -> SlackUser:
    """A reference to a Slack user.

    Args:
        identifier: The unique Slack user ID, email, or @mention for a Slack user, or a Sym :class:`~sym.sdk.user.User`
            instance. (e.g. "U12345", "jane\\@symops.io", "@Jane Austen").
        allow_self: A boolean indicating whether the requester may approve this Request.
        timeout: An integer representing the number of seconds for the request to remain active for this user. After
            timeout elapses, the request message will expire and can no longer be interacted with.
    """


def mention(identifier: Union[str, User]) -> str:
    """Returns a string that mentions a Slack user given their identifier.

    Users can be specified with a Slack user ID, email,
    a string version of an @mention. (e.g. "U12345", "jane\\@symops.io", "@Jane Austen", or a
    Sym :class:`~sym.sdk.user.User` instance).
    """


def channel(
    name: str, allow_self: bool = False, timeout: Optional[int] = None
) -> Union[SlackChannelID, SlackChannelName]:
    """A reference to a Slack channel.

    Args:
        name: The unique channel name or channel ID. (e.g. '#sym-requests' or 'C12345').
        allow_self: A boolean indicating whether the requester may approve this Request.
        timeout: An integer representing the number of seconds for the request to remain active for this user. After
            timeout elapses, the request message will expire and can no longer be interacted with.
    """


def group(
    users: Sequence[Union[str, User]], allow_self: bool = False, timeout: Optional[int] = None
) -> SlackUserGroup:
    """A reference to a Slack group DM.

    Args:
        users: A list of Slack Users to include in the group. Users can be specified with a Slack user ID, email,
            a string version of an @mention. (e.g. "U12345", "jane\\@symops.io", "@Jane Austen", or a
            Sym :class:`~sym.sdk.user.User` instance).
        timeout: An integer representing the number of seconds for the request to remain active for this user. After
            timeout elapses, the request message will expire and can no longer be interacted with.
    """


def fallback(
    *destinations: RequestDestination,
    continue_on_delivery_failure: Optional[bool] = True,
    continue_on_timeout: Optional[bool] = False,
) -> RequestDestinationFallback:
    """Returns a :class:`~sym.sdk.request_destination.RequestDestinationFallback` that contains the specified
    :class:`~sym.sdk.request_destination.RequestDestination` objects, with `continue_on_delivery_failure=True`.

    If used as the return value of a `get_approvers` reducer, when a Sym Request is made,
    each :class:`~sym.sdk.request_destination.RequestDestination` will be attempted in sequence until one succeeds.

    For example::

        def get_approvers(event):
            return slack.fallback(slack.channel("#missing"), slack.user("@david"))

    Args:
        destinations: At least 2 :class:`~sym.sdk.request_destination.RequestDestination` objects.
        continue_on_delivery_failure: A boolean representing whether to deliver to the next destination if a failure
            occurs while delivering to the current destination.
        continue_on_timeout: A boolean representing whether to deliver to the next destination if the Request at the
            current destination times out.
    """


def send_message(destination: Union[User, RequestDestination], message: str) -> None:
    """Sends a simple message to a destination in Slack. Accepts either a :class:`~sym.sdk.user.User`
    or a :class:`~sym.sdk.request_destination.RequestDestination`, which may represent a user, group, or channel
    in Slack.

    For example::

        # To send to #general:
        slack.send_message(slack.channel("#general"), "Hello, world!")

        # To DM a specific user:
        slack.send_message(slack.user("me@symops.io"), "It works!")

        # To DM the user who triggered an event:
        slack.send_message(event.user, "You did a thing!")

    Args:
        destination: Where the message should go.
        message: The text contents of the message to send.
    """


def send_thread_message(message: str) -> None:
    """Sends a simple message as a threaded reply to the current request message in Slack.

    Args:
        message: The text contents of the message to send.

    Raises:
        SlackError: If the current request was not sent to Slack via `get_request_notifications` or `get_approvers`,
            so there is no message to reply to.
    """


def get_user_info(user: User) -> dict:
    """Get information about a Slack user.

    Refer to Slack's users.info API documentation for the details on the response format:
    https://api.slack.com/methods/users.info

    Args:
        user: A Sym :class:`~sym.sdk.user.User` instance to get info about.
    """


def list_users(active_only: bool = True) -> list:
    """Returns a list of all users in the workspace.

    Refer to Slack's users.info API documentation for the details on the response format:
    https://api.slack.com/methods/users.list

    Args:
        active_only: A boolean indicating whether to exclude deactivated and deleted users.
    """


def is_user_in_group(user: User, *, group_id: str) -> bool:
    """Check if the provided :class:`~sym.sdk.user.User` is a member of the Slack user group specified.

    Login to Slack via web and retrieve the Slack user group ID in the left menu bar: `More` -> `People & user groups`
    -> `User groups` and select your user group. You can see the Slack user group ID in the URL:
    ``https://app.slack.com/client/{workspaceID}/browse-user-groups/user_groups/{usergroupID}``.

    If you have installed the Sym app before Aug 22nd 2023, then you may need to reinstall the Sym app to use this
    feature. Refer to the `main docs <https://docs.symops.com/docs/slack-app-integration#reinstall-slack-app>`_ for more details.

    Args:
        user: The :class:`~sym.sdk.user.User` to check group membership of.
        group_id: The ID of the Slack user group in which to search for the user.
    """


def users_in_channel(channel: Union[SlackChannelID, SlackChannelName, str]) -> List[User]:
    """Retrieves the users in a given Slack channel as a list of :class:`~sym.sdk.user.User` objects.

    "Channel" here includes all Slack conversation types, including public and private channels as well as groups.

    The ``channel`` argument can either be given as the output of the :func:`~sym.sdk.integrations.slack.channel`
    function, or as a string containing a Slack channel name or ID. If a channel name is given in a string, it must be
    prefixed with ``#``.

    The output is a list of :class:`~sym.sdk.user.User` objects, suitable for use in other areas of the Sym SDK. For
    example, to easily restrict the ability to approve or deny requests (including in the Sym webapp) to members of a
    Slack channel, one can use::

        @reducer
        def get_permissions(event):
            return RequestPermission(
                webapp_view=PermissionLevel.MEMBER,
                approve_deny=user_ids(slack.users_in_channel("#managers")),
                allow_self_approval=False
            )

    However, please see the "Cautions" below for some important caveats when using this function.

    (For more information on the ``get_permissions()`` reducer, please see `the docs
    <https://docs.symops.com/docs/reducers#get_permissions>`_.)

    **Cautions:**

    - Using this function introduces a hard dependency on Slack in your Sym Flow, which may have unintended effects; for
      example, during a Slack outage when the Slack API is unavailable. If you must use this function in such a way,
      wrap the call in a ``try``/``except`` block and include backup logic in the ``except`` block. In the above
      example, you may wish to set ``approve_deny=PermissionLevel.ADMIN`` in the ``except`` block, for instance, so that
      admins can still action requests in the webapp even if Slack is down.
    - This function may cause your Flow to experience a reducer timeout for large Slack channels, or if your Slack
      workspace has a very large number of total users or total channels. Test your usage to ensure that it works as
      expected. Using a channel ID instead of a channel name may improve performance.
    - To use this function with a private channel, the Sym app for Slack must be a member of that channel; otherwise,
      this function will raise a channel not found exception.
    - If this function is used with a Slack Connect channel or in a channel containing Slack guest users, any users from
      outside your organization *will* be included in the output.

    Args:
        channel: A ``SlackChannelID``, ``SlackChannelName``, or string representing the channel ID or name.

    Returns:
        A list of User objects representing the users in the channel, or an empty list if the channel is empty.

    Raises:
        :class:`~sym.sdk.exceptions.slack.SlackError`: If the channel is not found or another error occurs while
            interacting with the Slack API.
    """
