"""Defines the base Step class that will be used in Automations.

The Step should be imported into your script file along with Procedure. For each step in your
Procedure, you should create a subclass of step with a custom docstring that describes the manual
action for the user. Eventually when these Steps are being incrementally automated, overriding the
execute() method in the subclass will allow the Step to run code instead of just print the action.

Manual step example:
    # Define a Step subclass.
    class AWSLogin(Step):
        '''Login to AWS.

        https://844982026800.signin.aws.amazon.com/console/
        '''

    # Pass it to the Procedure.
    proc = Procedure([AWSLogin()], "Query DNS flushes.")
"""

from argparse import Namespace
from sys import exit as sys_exit
from loguru import logger
from .easy_doc import EasyDoc


class Step:
    """Step is one self contained unit of a Procedure.

    Attributes:
        number: The index of the Step in the Procedure's list.
        doc: An EasyDoc that wraps the class docstring.

    """

    def __init__(self, number: int) -> None:
        """Initialize, setting the number to 0, as the Procedure will number the Step."""
        logger.info("Initializing Step.")
        logger.debug(f"Passed number: {number}")

        self.number = number
        self.doc = EasyDoc(self.__doc__)

    def confirm(self) -> None:
        """Print a confirmation message for the user prompting them to confirm the Step."""
        try:
            input("    Press Enter to continue (Ctrl+c to quit):")
        except KeyboardInterrupt:
            print("\nExiting...")
            sys_exit(0)
        except EOFError:
            print("\nExiting...")
            sys_exit(0)

    def get_doc(self) -> str:
        """Print the Step's docstring, where the manual instructions for the step reside."""
        title = self.get_truncated()
        body = self.get_body()
        return f"\n{'-' * 80}\n{title}\n\n{body}\n"

    def get_truncated(self) -> str:
        """Print the first line of the Step's docstring."""
        return f"{self.number}) {self.doc.title}"

    def get_body(self) -> str:
        """Print the body of the Step's docstring."""
        return f"{self.doc.body}"

    def execute(self, context: Namespace) -> None:
        """Execute the Step.

        In the base class, this means just print the step and ask for confirmation. In subclasses,
        this method should be overriddent to automate the described action. Each Step's execute()
        method will be called in order by the Procedure when it is executing.

        """
        logger.info("Executing step")
        logger.debug(f"context: {context}")
        print(self.get_doc())
        self.confirm()
