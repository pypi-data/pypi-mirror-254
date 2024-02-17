import re
import uuid

import pytest
from pydantic import ValidationError

from sym.sdk import PermissionLevel, RequestPermission


class TestRequestPermission:
    user_ids_message = (
        "Invalid input. Use sym.sdk.user.user_ids() to convert List[User] to List[UUID]."
    )
    invalid_type_message = "Invalid input. Must be a PermissionLevel or List[UUID]. Use sym.sdk.user.user_ids() to convert List[User] to List[UUID]."

    def test_request_permissions_validation_happy_path(self):
        assert RequestPermission(webapp_view=[uuid.uuid4()], approve_deny=[uuid.uuid4()])
        assert RequestPermission(webapp_view=[str(uuid.uuid4())], approve_deny=[str(uuid.uuid4())])
        assert RequestPermission(
            webapp_view=PermissionLevel.MEMBER, approve_deny=PermissionLevel.ADMIN
        )
        assert RequestPermission(webapp_view="all_users", approve_deny="member")

    def test_request_permissions_validation_webapp_view_invalid_list(self):
        with pytest.raises(
            ValidationError,
            match=re.escape(self.user_ids_message),
        ):
            RequestPermission(webapp_view=["test@symops.io"], approve_deny=[uuid.uuid4()])

    def test_request_permissions_validation_webapp_view_invalid_role_enum(self):
        with pytest.raises(
            ValidationError,
            match=re.escape(self.invalid_type_message),
        ):
            RequestPermission(webapp_view="something else", approve_deny=[uuid.uuid4()])

    def test_request_permissions_validation_approve_deny_invalid_list(self):
        with pytest.raises(
            ValidationError,
            match=re.escape(self.user_ids_message),
        ):
            RequestPermission(webapp_view=[uuid.uuid4()], approve_deny=["test@symops.io"])

    def test_request_permissions_validation_approve_deny_invalid_role_enum(self):
        with pytest.raises(
            ValidationError,
            match=re.escape(self.invalid_type_message),
        ):
            RequestPermission(webapp_view=[uuid.uuid4()], approve_deny="something else")
