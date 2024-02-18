import json
from typing import Any, Dict, Optional
from uuid import uuid4

from sym.sdk import SRN, AccessTarget
from sym.sdk.strategies import Integration
from sym.sdk.strategy import Strategy


class IntegrationForTest(Integration):
    def __init__(self):
        super().__init__(srn="sym:integration:okta:test-okta-integration:latest")

    @property
    def type(self) -> str:
        return "okta"

    @property
    def external_id(self) -> str:
        return "symops-dev.okta.com"

    @property
    def settings(self) -> Dict[str, Any]:
        return {"api_token_secret": "12345"}


class AccessTargetForTest(AccessTarget):
    def __init__(self):
        super().__init__(srn="sym:access_target:okta:test-okta-target:latest")

    @property
    def label(self) -> Optional[str]:
        return None

    @property
    def type(self) -> str:
        return "okta"

    @property
    def settings(self) -> dict:
        return {"group_id": "012345"}


class TestStrategy:
    def test_strategy_to_json(self):
        integration = IntegrationForTest()
        target = AccessTargetForTest()
        strategy = Strategy(
            id=uuid4(),
            type="okta",
            name="test",
            integration=integration,
            targets=[target],
            settings={},
            srn=SRN.parse("sym:access_strategy:okta:test-okta-strategy:latest"),
        )

        assert strategy.json() == json.dumps(
            {
                "id": str(strategy.id),
                "type": "okta",
                "name": "test",
                "label": None,
                "integration": {
                    "external_id": "symops-dev.okta.com",
                    "name": "test-okta-integration",
                    "settings": {"api_token_secret": "12345"},
                    "type": "okta",
                },
                "targets": [
                    {"name": "test-okta-target", "settings": {"group_id": "012345"}, "type": "okta"}
                ],
                "settings": {},
                "srn": "sym:access_strategy:okta:test-okta-strategy:latest",
            }
        )
