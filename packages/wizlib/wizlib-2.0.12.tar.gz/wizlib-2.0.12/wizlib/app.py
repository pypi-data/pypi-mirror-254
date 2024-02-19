import sys
from dataclasses import dataclass
import os
from pathlib import Path

from wizlib.class_family import ClassFamily
from wizlib.command import WizHelpCommand
from wizlib.super_wrapper import SuperWrapper
from wizlib.parser import WizParser
from wizlib.ui import UI
from wizlib.ui.shell_ui import ShellUI


RED = '\033[91m'
RESET = '\033[0m'


class WizApp:
    """Root of all WizLib-based CLI applications. Subclass it. Can be
    instantiated and then run multiple commands."""

    base_command = None
    name = ''

    @classmethod
    def main(cls):  # pragma: nocover
        """Call this from a __main__ entrypoint"""
        cls.run(*sys.argv[1:], debug=os.getenv('DEBUG'))

    @classmethod
    def run(cls, *args, debug=False):
        """Call this from a Python entrypoint"""
        try:
            cls.initialize()
            app = cls(*args)
            command = app.first_command
            result = command.execute()
            if result:
                print(result, file=sys.stdout, end='')
                if sys.stdout.isatty():  # pragma: nocover
                    print()
            if command.status:
                print(command.status, file=sys.stderr)
        except Exception as error:
            if debug:
                raise error
            else:
                print(f"\n{RED}{type(error).__name__}: " +
                      f"{error}{RESET}\n", file=sys.stderr)
                sys.exit(1)

    @classmethod
    def initialize(cls):
        """Set up the app class to parse arguments"""
        cls.parser = WizParser(
            prog=cls.name,
            exit_on_error=False)
        for handler in cls.base_command.handlers:
            cls.parser.add_argument(
                f"--{handler.name}",
                f"-{handler.name[0]}",
                **handler.option_properties(cls))

        subparsers = cls.parser.add_subparsers(dest='command')
        for command in cls.base_command.family_members('name'):
            key = command.get_member_attr('key')
            aliases = [key] if key else []
            subparser = subparsers.add_parser(command.name, aliases=aliases)
            command.add_args(subparser)

    def __init__(self, *args):
        self.shell = ShellUI()
        args = args if args else [self.base_command.default]
        if not hasattr(self, 'parser'):
            self.__class__.initialize()
        self.vals = vars(self.parser.parse_args(args))
        self.first_command = self.get_command(**self.vals)

    def get_command(self, **vals):
        """Returns a single command"""
        if 'help' in vals:
            return WizHelpCommand(**vals)
        else:
            command_name = vals.pop('command')
            command_class = self.base_command.family_member(
                'name', command_name)
            if not command_class:
                raise Exception(f"Unknown command {command_name}")
            return command_class(**vals)
