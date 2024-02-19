from argparse import ArgumentParser
from pathlib import Path

from wizlib.class_family import ClassFamily
from wizlib.config_handler import ConfigHandler
from wizlib.input_handler import InputHandler
from wizlib.super_wrapper import SuperWrapper
from wizlib.ui import UI


class WizCommand(ClassFamily, SuperWrapper):
    """Define all the args you want, but stdin always works."""

    status = ''
    handlers = []
    ui: UI = None

    @classmethod
    def add_args(self, parser):
        """Add arguments to the command's parser - override this.
        Add global arguments in the base class. Not wrapped."""
        pass

    def __init__(self, **vals):
        for key in vals:
            setattr(self, key, vals[key])
        for handler in self.handlers:
            if handler.name not in vals:
                setattr(self, handler.name, handler())

    def handle_vals(self):
        """Clean up vals, calculate any, ask through UI, etc. - override
        this and call super().handle_vals()."""
        pass

    def provided(self, argument):
        """Was an argument provided?"""
        value = None
        if hasattr(self, argument):
            value = getattr(self, argument)
        return True if (value is False) else bool(value)

    def execute(self, method, *args, **kwargs):
        """Actually perform the command - override and wrap this via
        SuperWrapper"""
        self.handle_vals()
        result = method(self, *args, **kwargs)
        return result


class WizHelpCommand(WizCommand):

    def execute(self):
        return self.help
