"""Model representing a native Sym Strategy."""

from typing import Dict, List, Optional
from uuid import UUID

from pydantic import BaseModel

from sym.sdk.resource import SRN
from sym.sdk.strategies import Integration
from sym.sdk.target import AccessTarget


class Strategy(BaseModel):
    """The :class:`~sym.sdk.strategy.Strategy` class represents an instance of a ``sym_strategy`` resource.

    Read more about `Strategies <https://registry.terraform.io/providers/symopsio/sym/latest/docs/resources/strategy>`_.
    """

    class Config:
        arbitrary_types_allowed = True

        # To be able to call `.json` on a Strategy, we need to define a custom encoder because
        # Integrations, AccessTargets, and SRNs are not Pydantic models.
        #
        # For Integrations and AccessTargets, our custom encoder returns a dictionary, NOT
        # a JSON string, because otherwise it will be double encoded when the Strategy is JSON
        # dumped as a whole.
        json_encoders = {
            "Integration": lambda integration: integration.dict(),
            "AccessTarget": lambda target: target.dict(),
            "SRN": lambda srn: str(srn),
        }

    id: UUID
    """The unique ID of this Strategy."""

    type: str
    """The type of external service this Strategy manages access to.
    Corresponds to the ``type`` attribute on the ``sym_strategy`` resource.
    """

    name: str
    """The unique string identifier for this Strategy.
    Corresponds to the ``name`` attribute on the ``sym_strategy`` resource.
    """

    label: Optional[str] = None
    """An optional label for this Strategy."""

    integration: Integration
    """The :class:`~sym.sdk.strategies.integration.Integration` associated with this Strategy."""

    targets: List[AccessTarget] = []
    """The list of :class:`AccessTargets <sym.sdk.target.AccessTarget>` associated with this Strategy."""

    settings: Dict[str, str]
    """A map of settings specific to this Strategy.
    The possible settings available vary depending on the type of Strategy.
    """

    srn: SRN
    """The unique :class:`~sym.sdk.resource.SRN` for this Strategy."""
