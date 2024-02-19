from pathlib import Path
import sys

from wizlib.handler import Handler
from wizlib.ui import UI

# INTERACTIVE = sys.stdin.isatty()


class UIHandler(Handler):
    """A sort of proxy-handler for the UI class family, which drives user
    interactions (if any) during and between command execution. In this case,
    the handler only contains class-level methods, because the action actually
    returns the UI itself for the command to use."""

    name = 'ui'

    @classmethod
    def option_properties(cls, app):
        """Argparse keyword arguments for this optional arg"""
        return {
            # 'choices': ['shell'],
            'default': 'shell',
            'help': 'Only option currently is "shell" (the default)',
            'type': cls.ui
        }

    @classmethod
    def ui(cls, uitype):
        """Instead of instantiating the handler, return the chosen UI
        object."""
        return UI.family_member('name', uitype)()
