#!/usr/bin/python3

""" Module for TestHBNBCommand class """

from console import HBNBCommand
from models.engine.file_storage import FileStorage
import unittest
import datetime
from unittest.mock import patch
import sys
from io import StringIO
import re
import os

class TestHBNBCommand(unittest.TestCase):

    """Tests HBNBCommand console."""

    # Your test methods here...

    def setUp(self):
        """Sets up test cases."""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        self.resetStorage()
