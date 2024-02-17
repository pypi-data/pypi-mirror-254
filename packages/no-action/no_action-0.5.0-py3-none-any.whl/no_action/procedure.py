"""Defines the Procedure class that wraps an ordered list of Steps.

The Procedure also handles enumerating the steps.

Typical usage:
    my_proc = Procedure(steps = [StepA(), StepB()], title = "Expand storage.")
    my_proc.execute()
"""

from __future__ import annotations
from argparse import ArgumentParser, Namespace
from datetime import datetime
from sys import exit
from jinja2 import Environment, PackageLoader, TemplateNotFound

from .exceptions import UnsupportedOutputException


class Procedure:
    """A wrapper around steps that have a specific order.

    Attributes:
        context: A Object-like container of arguments and variables for Steps.
        description: A longer description of the procedure. Printed before the steps.
        step_list: A list of Step derived classes which will be executed.
        title: The name of the Procedure. Printed at the top of the procedure run.

    """

    def __init__(self, steps: list[type], title: str, description: str = "") -> None:
        """Initialize a Procedure with a title, steps, and optional description.

        The Steps will pass through an initialization page where information from the Procedure is
        shared to all Steps. Initialization will enumerate each step.

        Args:
            steps: A list of Step derived classes that make up the procedure.
            title: The name of the Procedure. Printed at the top of the procedure run.
            description: A longer description of the procedure. Printed before the steps.

        """
        self.title = title
        self.description = description
        self.step_list = []
        self._argparser: ArgumentParser = ArgumentParser(description=self.title)

        self.__register_default_arguments()
        self.context: Namespace = self._argparser.parse_args()

        # Add the program call name to the context.
        self.context.prog = self._argparser.prog

        self.__initialize_steps(steps)

        if self.context.list:
            # If --list argument
            self.__list_steps()
        elif self.context.output_sop:
            # If --output-sop
            self.__output_sop(self.context.output_sop)

    def __initialize_steps(self, steps: list[type]) -> None:
        """Initialize each step by feeding it its index in the procedure list and the context.

        Args:
            steps: A list of Step derived classes that make up the procedure.

        """
        for i, step in enumerate(steps):
            temp = step(i + 1, self.context)
            self.step_list.append(temp)

    def __list_steps(self) -> None:
        """Print a short description of each Step and exit."""
        print(f"Procedure: {self.title}\n\n")
        print(self.description + "\n\n")
        print("Steps:\n")
        for s in self.step_list:
            print(s.get_truncated())
        exit(0)

    def __output_sop(self, format: str) -> None:
        """Use Jinja to format the output based on templates.

        Args:
            format: Either 'md' or 'rst'

        """
        jinja_env = Environment(
            auto_reload=False,
            lstrip_blocks=True,
            loader=PackageLoader("no_action"),
            trim_blocks=True,
        )
        try:
            template = jinja_env.get_template(f"output.{format}.j2")
        except TemplateNotFound as err:
            # TODO log an error here.
            raise UnsupportedOutputException(f"The format {format} is unsupported.") from err

        print(template.render(procedure=self, now=datetime.utcnow()))
        exit(0)

    def __register_default_arguments(self) -> None:
        """Register default command line args that the Procedure will catch and execute on."""
        # List the steps
        self._argparser.add_argument(
            "-l",
            "--list",
            action="store_true",
            default=False,
            help="print a short description of each Step and exit",
        )

        # Version output
        self._argparser.add_argument(
            "-v", "--version", action="version", version="no_action v0.1.0"
        )

        # Output format
        self._argparser.add_argument(
            "--output-sop",
            choices=["md", "rst"],
            help="output Procedure details and full steps in format",
        )

    def execute(self) -> None:
        """Print Procedure information then print each step."""
        print(f"Procedure: {self.title}\n\n")
        print(self.description + "\n\n")
        print("Steps:")

        for step in self.step_list:
            step.execute()

        print("Done.")
