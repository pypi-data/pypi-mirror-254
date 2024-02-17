"""Helpers for interacting with the Sym platform itself from within the Sym SDK."""

from typing import List

from sym.sdk.user import User


def get_or_create_user_by_email(email: str) -> User:
    """For the given email address, retrieve the Sym :class:`~sym.sdk.user.User` if one exists, or create a new Sym
    ``User`` if none exists.

    If the user was not found and could not be created, or another error occurred (e.g., an invalid email address was
    specified), this function will instead raise an exception. It will never return ``None``.

    Args:
        email: The email address of the user to retrieve or create.

    Returns:
        The Sym :class:`~sym.sdk.user.User` corresponding to the given email address.

    Raises:
        :class:`~sym.sdk.exceptions.sym_integration.SymIntegrationError`: If the user could not be retrieved or created,
            or if the email address is invalid, or on any other error.
    """


def get_or_create_users_by_emails(emails: List[str], raise_on_error: bool = False) -> List[User]:
    """For each of the given list of email addresses, retrieve the corresponding Sym :class:`~sym.sdk.user.User` if one
    exists, or create a new one otherwise.

    If ``raise_on_error`` is ``True``, then any "routine" errors that occur while processing the list of emails (for
    example, an invalid email was specified or a user could not be found and failed to be created) will be raised as an
    exception. Otherwise, the errors will be logged as warnings and the corresponding user will be omitted from the
    output. The returned list of users will never contain ``None``\\ s.

    Regardless of the value of ``raise_on_error``, serious errors (such as a communication failure within the Sym
    platform or malformed input) will always be raised as exceptions.

    Args:
        emails: A list of email addresses of the users to retrieve or create. Must not contain any ``None`` values.
        raise_on_error: Whether to raise an exception if an error occurs while processing the list of emails. If
            ``False``, errors will be logged as warnings and the corresponding user will be omitted from the output.
            Defaults to ``False``.

    Returns:
        A list of Sym :class:`~sym.sdk.user.User`\\ s corresponding to the given email addresses.

    Raises:
        :class:`~sym.sdk.exceptions.sym_integration.SymIntegrationError`: If ``raise_on_error`` is ``True`` and any
            errors occur while processing the list of emails, or if any other error occurs.
    """
