"""Defines the Procedure class that wraps an ordered list of Steps.

The Procedure also handles enumerating the steps.

Typical usage:
    my_proc = Procedure(steps = [StepA(), StepB()], title = "Expand storage.")
    my_proc.execute()
"""

from __future__ import annotations
from argparse import ArgumentParser, Namespace
from datetime import datetime
from sys import exit as sys_exit, stderr
from importlib.metadata import version
from jinja2 import Environment, PackageLoader, TemplateNotFound
from loguru import logger

from .step import Step
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
        self._verstr: str = version("no_action")

        self.title = title
        self.description = description
        self.step_list: list[Step] = []
        self._argparser: ArgumentParser = ArgumentParser(description=self.title)

        self.__register_default_arguments()
        self.context: Namespace = self._argparser.parse_args()

        # Set logger sink verbosity
        self.__setup_logger()
        logger.info("Initializing Procedure")
        logger.debug(f"steps passed: {steps}")

        # Add the program call name to the context.
        self.context.prog = self._argparser.prog

        # Add the version number to the context.
        self.context.version = f"no_action {self._verstr}"

        logger.info("Command line arguments parsed.")
        logger.debug(f"Context Namespace is: {self.context}")

        self.__initialize_steps(steps)

        if self.context.list:
            logger.info("--list is present")
            self.__list_steps()
        elif self.context.output_sop:
            logger.info(f"--output-sop is present: {self.context.output_sop}")
            self.__output_sop(self.context.output_sop)

    def __setup_logger(self) -> None:
        log_levels: list[str] = ["CRITICAL", "WARNING", "INFO", "DEBUG"]

        # Ensure verbosity level isn't out of bounds
        verbosity = min(self.context.verbosity, len(log_levels) - 1)

        logger.configure(
            handlers=[
                {"sink": stderr, "level": log_levels[verbosity], "diagnose": False}
            ],
            activation=[("", False), ("no_action", True)],
        )
        logger.info("Logger initialized")

    def __initialize_steps(self, steps: list[type]) -> None:
        """Initialize each step by feeding it its index in the procedure list.

        Args:
            steps: A list of Step derived classes that make up the procedure.

        """
        logger.info("Initializing steps")
        for i, step in enumerate(steps):
            temp = step(i + 1)
            self.step_list.append(temp)
        logger.info("Steps Initialized")
        logger.debug(f"Post-initialization step_list: {self.step_list}")

    def __list_steps(self) -> None:
        """Print a short description of each Step and exit."""
        print(f"Procedure: {self.title}\n\n")
        print(self.description + "\n\n")
        print("Steps:\n")
        for s in self.step_list:
            print(s.get_truncated())
        logger.info("Exiting after listing all steps.")
        sys_exit(0)

    def __output_sop(self, style: str) -> None:
        """Use Jinja to format the output based on templates.

        Args:
            style: Either 'md' or 'rst' or 'confwiki'

        """
        jinja_env = Environment(
            auto_reload=False,
            lstrip_blocks=True,
            loader=PackageLoader("no_action"),
            trim_blocks=True,
        )
        try:
            logger.info("Loading requested template.")
            template = jinja_env.get_template(f"output.{style}.j2")
        except TemplateNotFound as err:
            logger.error(
                f"Provided format: '{style}' does not have a corresponding template."
            )
            raise UnsupportedOutputException(
                f"The format {style} is unsupported."
            ) from err

        logger.info("Jinja rendering template.")
        print(template.render(procedure=self, now=datetime.utcnow()))
        logger.info("Template rendered to screen")
        logger.info("Existing after successful render")
        sys_exit(0)

    def __register_default_arguments(self) -> None:
        """Register default command line args that the Procedure will catch and execute on."""
        # List the steps
        self._argparser.add_argument(
            "--list",
            action="store_true",
            default=False,
            help="print a short description of each Step and exit",
        )

        # Version output
        self._argparser.add_argument(
            "--version", action="version", version=self._verstr
        )

        # Output format
        self._argparser.add_argument(
            "--output-sop",
            choices=["md", "rst", "conwiki"],
            help="output Procedure details and full steps in format",
        )

        self._argparser.add_argument(
            "-v",
            action="count",
            default=0,
            dest="verbosity",
            help="enable logging levels from 0 to 3",
        )

    def execute(self) -> None:
        """Print Procedure information then print each step."""
        logger.info("Executing procedure")
        print(f"Procedure: {self.title}\n\n")
        print(self.description + "\n\n")
        print("Steps:")

        for step in self.step_list:
            logger.info("Executing step {}", step)
            step.execute(self.context)

        print("Done.")
