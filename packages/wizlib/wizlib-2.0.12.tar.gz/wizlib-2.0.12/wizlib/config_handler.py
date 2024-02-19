from argparse import Namespace
from pathlib import Path
import os
from dataclasses import dataclass
from unittest.mock import patch

from yaml import load
from yaml import Loader
from wizlib.handler import Handler

from wizlib.error import ConfigHandlerError


class ConfigHandler(Handler):
    """
    Handle app-level configuration, where settings could come from specific
    settings (such as from argparse), environment variables, or a YAML file.
    Within the Python code, config keys are underscore-separated all-lower.

    A ConfigHandler returns null in the case of a missing value, assuming that
    commands can handle their own null cases.
    """

    name = 'config'

    def __init__(self, value=None):
        self.file = value
        self.cache = {}

    @property
    def yaml(self):
        if hasattr(self, '_yaml'):
            return self._yaml
        path = None
        if self.file:
            path = Path(self.file)
        elif self.appname:
            localpath = Path.cwd() / f".{self.appname}.yml"
            homepath = Path.home() / f".{self.appname}.yml"
            if (envvar := self.env(self.appname + '-config')):
                path = Path(envvar)
            elif (localpath.is_file()):
                path = localpath
            elif (homepath.is_file()):
                path = homepath
        if path:
            with open(path) as file:
                self._yaml = load(file, Loader=Loader)
                return self._yaml

    @staticmethod
    def env(name):
        if (envvar := name.upper().replace('-', '_')) in os.environ:
            return os.environ[envvar]

    def get(self, key: str):
        """Return the value for the requested config entry"""

        # If we already found the value, return it
        if key in self.cache:
            return self.cache[key]

        # Environment variables take precedence
        if (result := self.env(key)):
            self.cache[key] = result
            return result

        # Otherwise look at the YAML
        if (yaml := self.yaml):
            split = key.split('-')
            while (val := split.pop(0)) and (val in yaml):
                yaml = yaml[val] if val in yaml else None
                if not split:
                    self.cache[key] = yaml
                    return yaml

    @classmethod
    def fake(cls, **vals):
        """Return a fake ConfigHandler with forced values, for testing"""
        handler = cls()

        def fake_env(name):
            key = name.replace('-', '_')
            if key in vals:
                return vals[key]
        handler.env = fake_env
        return handler
