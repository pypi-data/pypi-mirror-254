"""Defines the EasyDoc class that will be used to parse the docstring of a Step.

EasyDoc parses and provides sane attributes for various parts of the docstring.
"""

from inspect import cleandoc
from typing import Optional
from loguru import logger

from .exceptions import MissingDocstringException


class EasyDoc:
    """EasyDoc parses and exposes parts of a docstring.

    Attributes:
        original:
            The original text passed in.
        cleaned_original:
            Original docstring that has the indentation removed.
        title:
            The first line of the docstring.
        body:
            The body of the docstring.

    """

    def __init__(self, doc: Optional[str]) -> None:
        """Initialize and ingest the original doc and call parsing functions.

        Args:
            doc: The docstring.

        Raises:
            MissingDocstringException

        """
        logger.info("Initialize the EasyDoc")
        try:
            assert doc is not None
            logger.debug(f"Passed docstring: {doc}")
            self.original: str = doc
            # Clean the whitespace
            self.cleaned_original: str = cleandoc(doc)

            self.__parse_title()
            self.__parse_body()
        except AssertionError as err:
            logger.error("The docstring is empty, cannot parse.")
            raise MissingDocstringException("Docstring is empty.") from err

    def __parse_title(self) -> None:
        # Attempt to split out the first line only.
        splits: list[str] = self.cleaned_original.split(sep="\n", maxsplit=1)
        if len(splits):
            if splits[0]:
                self.title: str = splits[0]
                logger.info(f"title: {self.title}")

    def __parse_body(self) -> None:
        # Split out the body only.
        splits: list[str] = self.cleaned_original.split(sep="\n", maxsplit=1)
        if len(splits):
            del splits[0]
            self.body: str = "\n".join(splits)
            logger.info(f"body: {self.body}")
