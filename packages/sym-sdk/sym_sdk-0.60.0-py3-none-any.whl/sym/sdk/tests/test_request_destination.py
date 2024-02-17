import json
from unittest.mock import patch

import pytest

from sym.sdk import SlackChannelID, SlackChannelName, SlackUser, SlackUserGroup
from sym.sdk.request_destination import RequestDestination


class TestRequestDestination:
    @pytest.mark.parametrize("lookup_type", ["user", "user_id", "username", "channel", "email"])
    def test_old_slack_models_parse_into_request_destinations(self, lookup_type: str):
        """Ensures we don't make breaking changes to how we parse SlackRequestDestination models,
        since older requests may have the older models saved in state.

        The older lookup types were::

            class SlackLookupType(ChoiceEnum):
                USER = "user"  # sym.sdk.User object
                USER_ID = "user_id"  # e.g. U12345
                USERNAME = "username"  # eg. @First Last
                CHANNEL = "channel"  # e.g. C12345
                EMAIL = "email"  # e.g. user@symops.io

        Where the lookup type determined the type of data stored in `lookup_keys`, which was a list.
        For example::

            {"lookup_type": "channel", "lookup_keys": ["#sym-requests"], "allow_self": True}
        """

        data = json.dumps(
            {
                "lookup_type": lookup_type,
                # The only reason we'd be reading these legacy models is to check for `allow_self`.
                # Any other data is incompatible with the way we use the new models, so that is already broken
                # and we won't worry about it.
                "lookup_keys": ["doesntmatter"],
                "allow_self": True,
            }
        )

        destination = RequestDestination.parse_raw(data)
        assert isinstance(destination, RequestDestination)
        assert destination.allow_self

    def test_slack_channel_id_succeeds_for_valid_channel_ids(self):
        assert SlackChannelID(channel_id="C12345").channel_id == "C12345"
        assert SlackChannelID(channel_id="D12345").channel_id == "D12345"
        assert SlackChannelID(channel_id="G12345").channel_id == "G12345"
        assert SlackChannelID(channel_id="  C12345 ").channel_id == "C12345"

    @pytest.mark.parametrize(
        "channel_id, match_error",
        [
            ("", "must be non-empty"),
            (" ", "must be non-empty"),
            ("X123", "not a valid Slack Channel ID"),
        ],
    )
    def test_slack_channel_id_validate_channel_id_format_throws_error_if_not_valid_channel_id(
        self, channel_id, match_error
    ):
        with pytest.raises(ValueError, match=match_error):
            SlackChannelID(channel_id=channel_id)

    def test_slack_channel_id__str__(self):
        assert SlackChannelID(channel_id="C12345").__str__() == "SlackChannelID 'C12345'"
        assert SlackChannelID(channel_id="D12345").__str__() == "SlackChannelID 'D12345'"
        assert SlackChannelID(channel_id="G12345").__str__() == "SlackChannelID 'G12345'"
        assert SlackChannelID(channel_id="  C12345 ").__str__() == "SlackChannelID 'C12345'"

    def test_slack_channel_name_succeeds_if_channel_name_exists(self):
        assert (
            SlackChannelName(channel_name="is-valid-channel-name").channel_name
            == "is-valid-channel-name"
        )
        assert (
            SlackChannelName(channel_name="  is-valid-channel-name  ").channel_name
            == "is-valid-channel-name"
        )

    @pytest.mark.parametrize(
        "channel_name, match_error",
        [
            ("", "channel_name must be non-empty"),
            (" ", "channel_name must be non-empty"),
        ],
    )
    def test_slack_channel_name_throws_error_when_no_value_given(self, channel_name, match_error):
        with pytest.raises(ValueError, match=match_error):
            SlackChannelName(channel_name=channel_name)

    def test_slack_channel_name__str__(self):
        assert (
            SlackChannelName(channel_name="is-valid-channel-name").__str__()
            == "SlackChannelName 'is-valid-channel-name'"
        )
        assert (
            SlackChannelName(channel_name="  is-valid-channel-name  ").__str__()
            == "SlackChannelName 'is-valid-channel-name'"
        )

    def test_slack_user_succeeds_if_valid(self):
        assert SlackUser(user_id="W09876").user_id == "W09876"
        assert SlackUser(user_id="U12345").user_id == "U12345"
        assert SlackUser(user_id="  U12345  ").user_id == "U12345"

    @pytest.mark.parametrize(
        "user_id, match_error",
        [
            ("", "user_id must be non-empty"),
            (" ", "user_id must be non-empty"),
            (
                "X123",
                "X123 is not a valid Slack User ID. Slack User IDs must start with 'U' or 'W'.",
            ),
        ],
    )
    def test_slack_user_throws_error_if_invalid_user_id(self, user_id, match_error):
        with pytest.raises(ValueError, match=match_error):
            SlackUser(user_id=user_id)

    def test_slack_user__str__(self):
        assert SlackUser(user_id="U12345").__str__() == "SlackUser 'U12345'"
        assert SlackUser(user_id="  U12345  ").__str__() == "SlackUser 'U12345'"

    def test_slack_user_mention(self):
        assert SlackUser(user_id="U12345").mention() == "<@U12345>"
        assert SlackUser(user_id="  U12345  ").mention() == "<@U12345>"

    def test_slack_user_group_if_valid(self):
        assert SlackUserGroup(users=[SlackUser(user_id="U12345")]).users == [
            SlackUser(user_id="U12345")
        ]

    @pytest.mark.parametrize(
        "users, match_error",
        [
            ([], "at least 1 items"),
            (
                [
                    SlackUser(user_id="U1"),
                    SlackUser(user_id="U2"),
                    SlackUser(user_id="U3"),
                    SlackUser(user_id="U4"),
                    SlackUser(user_id="U5"),
                    SlackUser(user_id="U6"),
                    SlackUser(user_id="U7"),
                    SlackUser(user_id="U8"),
                ],
                "at most 7 items",
            ),
        ],
    )
    def test_slack_user_group_throws_error_if_invalid(self, users, match_error):
        with pytest.raises(ValueError, match=match_error):
            SlackUserGroup(users=users)

    def test_slack_user_group__str__(self):
        slack_user_group = SlackUserGroup(
            users=[SlackUser(user_id="U12345"), SlackUser(user_id="U6789")]
        )
        assert slack_user_group.__str__() == "SlackUserGroup '['U12345', 'U6789']'"

    @pytest.mark.parametrize("parse_raw", [True, False])
    def test_slack_channel_id__parse(self, parse_raw):
        data = SlackChannelID(channel_id="C12345")

        if parse_raw:
            data = data.json()
            slack_channel_id = SlackChannelID.parse_raw(data)
        else:
            data = data.dict()
            slack_channel_id = SlackChannelID.parse_obj(data)

        for klass in {RequestDestination, SlackChannelID}:
            slack_channel_id = klass.parse_raw(data) if parse_raw else klass.parse_obj(data)
            assert isinstance(slack_channel_id, SlackChannelID)
            assert slack_channel_id.channel_id == "C12345"

    @pytest.mark.parametrize("parse_raw", [True, False])
    def test_slack_channel_name__parse(self, parse_raw):
        data = SlackChannelName(channel_name="#general")

        if parse_raw:
            data = data.json()
            slack_channel_name = SlackChannelName.parse_raw(data)
        else:
            data = data.dict()
            slack_channel_name = SlackChannelName.parse_obj(data)

        for klass in {RequestDestination, SlackChannelName}:
            slack_channel_name = klass.parse_raw(data) if parse_raw else klass.parse_obj(data)
            assert isinstance(slack_channel_name, SlackChannelName)
            assert slack_channel_name.channel_name == "#general"

    @pytest.mark.parametrize("parse_raw", [True, False])
    def test_slack_user__parse(self, parse_raw):
        data = SlackUser(user_id="U12345")

        if parse_raw:
            data = data.json()
            slack_user = SlackUser.parse_raw(data)
        else:
            data = data.dict()
            slack_user = SlackUser.parse_obj(data)

        for klass in {RequestDestination, SlackUser}:
            slack_user = klass.parse_raw(data) if parse_raw else klass.parse_obj(data)
            assert isinstance(slack_user, SlackUser)
            assert slack_user.user_id == "U12345"

    @pytest.mark.parametrize("parse_raw", [True, False])
    def test_slack_user_group__parse(self, parse_raw):
        data = SlackUserGroup(users=[SlackUser(user_id="U12345"), SlackUser(user_id="U6789")])

        if parse_raw:
            data = data.json()
            slack_user_group = SlackUserGroup.parse_raw(data)
        else:
            data = data.dict()
            slack_user_group = SlackUserGroup.parse_obj(data)

        for klass in {RequestDestination, SlackUserGroup}:
            slack_user_group = klass.parse_raw(data) if parse_raw else klass.parse_obj(data)
            assert isinstance(slack_user_group, SlackUserGroup)
            assert isinstance(slack_user_group.users[0], SlackUser)
            assert slack_user_group.users[0].user_id == "U12345"
            assert isinstance(slack_user_group.users[1], SlackUser)
            assert slack_user_group.users[1].user_id == "U6789"

    def test_request_destination__parse_obj_fails_for_unknown_type(self):
        data = {"bogus": "#general"}

        with pytest.raises(ValueError, match="Unknown type of RequestDestination"):
            RequestDestination.parse_obj(data)

    @patch("sym.sdk.request_destination.SlackChannelName.__init__", side_effect=Exception("boom!"))
    def test_request_destination__parse_obj_fails_for_unexpected_error(self, _):
        data = {"channel_name": "#general"}

        with pytest.raises(ValueError, match="Failed to parse RequestDestination data: boom!"):
            RequestDestination.parse_obj(data)
