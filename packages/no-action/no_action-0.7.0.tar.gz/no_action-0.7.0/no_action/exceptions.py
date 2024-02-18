"""Defines expections that no_action will use."""


class MissingDocstringException(Exception):
    """Raise when the docstring is empty."""


class UnsupportedOutputException(Exception):
    """Raise when there is no corresponding Jinja2 template file for the requested format."""
