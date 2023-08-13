#!/usr/bin/python3
"""Unit tests for city class"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test Cases for the User class."""

    def test_instantiation(self):
        """Test instantiation of User class."""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)

    def test_attributes(self):
        """Testt attributes of User class."""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))


if __name__ == "__main__":
    unittest.main()
