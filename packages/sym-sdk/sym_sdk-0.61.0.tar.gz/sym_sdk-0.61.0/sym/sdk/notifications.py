"""Model for configuring where to send messages when a Request is created."""

from typing import List, Optional, Union

from pydantic import BaseModel, Field, validator

from sym.sdk.user import User

from .request_destination import RequestDestination, SlackRequestDestination


class Notification(BaseModel):
    """Configuration for where to send a message when a Request is created.

    A :class:`~sym.sdk.notifications.Notification` will be considered "failed to deliver" if:
        - None of the destinations can be sent to, for any reason.
        - The timeout is reached without any action taken on it.
    """

    class Config:
        arbitrary_types_allowed = True

        # To be able to call `.json` on a Notification with a User in it, we need to define a custom
        # encoder because Users are not Pydantic models. Our custom encoder returns a dictionary, NOT
        # a JSON string, because otherwise it will be double encoded when the Notification is JSON
        # dumped as a whole.
        json_encoders = {
            "User": lambda u: u.to_dict(),
        }

    destinations: List[Union[RequestDestination, User]] = Field(min_items=1)
    """A list of :class:`RequestDestinations <~sym.sdk.request_destination.RequestDestination>`
    to which Sym will attempt to send this notification.
    """

    timeout: Optional[int] = None
    """Tne number of seconds until this notification will time out if no action is taken on it.
    If not specified, the notification will never time out.
    """

    @validator("destinations")
    def ensure_only_one_slack_destination(cls, value):
        """This validator enforces the constraint that only one Slack
        :class:`~sym.sdk.request_destination.RequestDestination` is allowed per
        :class:`~sym.sdk.notifications.Notification`.
        """

        if sum(isinstance(destination, SlackRequestDestination) for destination in value) > 1:
            raise ValueError("Only one SlackRequestDestination is allowed per Notification.")

        return value
