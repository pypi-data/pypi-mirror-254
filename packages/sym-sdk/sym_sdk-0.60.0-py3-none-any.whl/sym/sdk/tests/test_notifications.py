import json
from datetime import datetime
from typing import Dict, List, Literal, Optional
from uuid import UUID, uuid4

import pytest
from pydantic import ValidationError

from sym.sdk.notifications import Notification
from sym.sdk.request_destination import SlackChannelID, SlackChannelName, SlackUser, SlackUserGroup
from sym.sdk.user import User, UserIdentity, UserRole


class UserForTest(User):
    """A minimal concrete child of User for testing serialization."""

    def __init__(self):
        self._id = uuid4()

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def email(self) -> Optional[str]:
        return "testuser@symops.invalid"

    @property
    def username(self) -> str:
        return "testuser@symops.invalid"

    @property
    def type(self) -> str:
        return "normal"

    @property
    def first_name(self) -> Optional[str]:
        return "Test"

    @property
    def last_name(self) -> Optional[str]:
        return "User"

    @property
    def identities(self) -> Dict[str, List[UserIdentity]]:
        return {}

    @property
    def role(self) -> UserRole:
        return UserRole.MEMBER

    def identity(
        self,
        service_type: str,
        service_id: Optional[str] = None,
    ) -> Optional[UserIdentity]:
        return None

    def get_event_count(
        self,
        event_name,
        since: Optional[datetime] = None,
        until: Optional[datetime] = None,
        filter_on: Literal["flow", "target"] = "flow",
        include_errored: bool = False,
    ) -> int:
        return 0

    def to_dict(self) -> dict:
        """This would normally be inherited from SDKUser in the Runtime, but that is not available here,
        so we will hard code it for testing purposes.
        """
        return {"id": str(self.id), "username": self.username}


class TestNotification:
    def test_destinations__at_least_one_required(self):
        with pytest.raises(ValidationError):
            Notification(destinations=[])

    def test_destinations__only_one_slack_destination_allowed(self):
        assert Notification(destinations=[SlackChannelName(channel_name="#general")])

        with pytest.raises(ValidationError):
            Notification(
                destinations=[
                    SlackChannelName(channel_name="#sym-errors"),
                    SlackChannelName(channel_name="#general"),
                ]
            )

        with pytest.raises(ValidationError):
            Notification(
                destinations=[
                    SlackChannelName(channel_name="#general"),
                    SlackUser(user_id="U12345"),
                ]
            )

    @pytest.mark.parametrize("parse_raw", [True, False])
    def test_notification__parse_with_slack_user_group(self, parse_raw: bool):
        data = Notification(
            destinations=[
                SlackUserGroup(users=[SlackUser(user_id="U12345"), SlackUser(user_id="U6789")])
            ]
        )

        if parse_raw:
            data = data.json()
            notification = Notification.parse_raw(data)
        else:
            data = data.dict()
            notification = Notification.parse_obj(data)

        assert isinstance(notification, Notification)
        assert isinstance(notification.destinations[0], SlackUserGroup)
        assert isinstance(notification.destinations[0].users[0], SlackUser)
        assert notification.destinations[0].users[0].user_id == "U12345"
        assert isinstance(notification.destinations[0].users[1], SlackUser)
        assert notification.destinations[0].users[1].user_id == "U6789"

    @pytest.mark.parametrize("parse_raw", [True, False])
    def test_notification__parse_with_slack_user(self, parse_raw):
        data = Notification(destinations=[SlackUser(user_id="U12345")])

        if parse_raw:
            data = data.json()
            notification = Notification.parse_raw(data)
        else:
            data = data.dict()
            notification = Notification.parse_obj(data)

        assert isinstance(notification, Notification)
        assert isinstance(notification.destinations[0], SlackUser)
        assert notification.destinations[0].user_id == "U12345"

    @pytest.mark.parametrize("parse_raw", [True, False])
    def test_notification__parse_with_slack_channel_name(self, parse_raw):
        data = Notification(destinations=[SlackChannelName(channel_name="#general")])

        if parse_raw:
            data = data.json()
            notification = Notification.parse_raw(data)
        else:
            data = data.dict()
            notification = Notification.parse_obj(data)

        assert isinstance(notification, Notification)
        assert isinstance(notification.destinations[0], SlackChannelName)
        assert notification.destinations[0].channel_name == "#general"

    @pytest.mark.parametrize("parse_raw", [True, False])
    def test_notification__parse_with_slack_channel_id(self, parse_raw):
        data = Notification(destinations=[SlackChannelID(channel_id="C12345")])

        if parse_raw:
            data = data.json()
            notification = Notification.parse_raw(data)
        else:
            data = data.dict()
            notification = Notification.parse_obj(data)

        assert isinstance(notification, Notification)
        assert isinstance(notification.destinations[0], SlackChannelID)
        assert notification.destinations[0].channel_id == "C12345"

    def test_notification__to_json(self):
        user = UserForTest()
        data = Notification(destinations=[SlackChannelName(channel_name="#general"), user])

        assert data.json() == json.dumps(
            {
                "destinations": [
                    {
                        "allow_self": False,
                        "timeout": None,
                        "channel_name": "#general",
                    },
                    {"id": str(user.id), "username": user.username},
                ],
                "timeout": None,
            }
        )
