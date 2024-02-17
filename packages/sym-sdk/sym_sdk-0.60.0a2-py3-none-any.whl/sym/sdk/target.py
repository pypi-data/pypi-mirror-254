"""An instance of a `sym_target` to request access to."""

from abc import ABC, abstractmethod
from typing import Optional

from sym.sdk.resource import SymResource


class AccessTarget(SymResource, ABC):
    """The :class:`~sym.sdk.target.AccessTarget` class represents an instance
    of a `sym_target` that a :class:`~sym.sdk.user.User` can request access to.

    Read more about `Targets <https://registry.terraform.io/providers/symopsio/sym/latest/docs/resources/target>`_.
    """

    @property
    @abstractmethod
    def label(self) -> Optional[str]:
        """The display name for this :class:`~sym.sdk.target.AccessTarget`."""

    @property
    @abstractmethod
    def type(self) -> str:
        """The type of resource to be accessed (e.g., "okta_group", "aws_iam_group")."""

    @property
    @abstractmethod
    def settings(self) -> dict:
        """The dictionary of settings from :class:`~sym.sdk.target.AccessTarget`'s
        definition in Terraform.
        """
