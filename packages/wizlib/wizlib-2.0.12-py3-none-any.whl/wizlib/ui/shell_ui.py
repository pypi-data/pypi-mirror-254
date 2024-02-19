import sys

from readchar import readkey
from wizlib.rlinput import rlinput
from wizlib.ui import UI


class ShellUI(UI):

    """The UI to execute one command passed in through the shell. There will be
    limited interactivity, if the user omits an argument on the command line,
    but otherwise this is a run and done situation.
    """

    name = "shell"

    def send(self, value: str):
        """Output some text"""
        if value:
            print(value, file=sys.stderr)

    def get_option(self, chooser):
        """Get a choice from the user with a single keystroke"""
        # key = rlinput(chooser.prompt_string)
        print(chooser.prompt_string, end='', file=sys.stderr, flush=True)
        if sys.stdin.isatty():
            key = readkey()
        else:
            key = input()
        print(file=sys.stderr, flush=True)
        return chooser.choice_by_key(key)
