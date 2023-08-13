#!/usr/bin/python3

"""Unittest module for the Amenity Class."""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    """Test Cases for the Amenity class."""

    def test_instantiation(self):
        """Tests instantiation of Amenity class."""
        amenity = Amenity()
        self.assertEqual(str(type(amenity)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(issubclass(type(amenity), BaseModel))


if __name__ == "__main__":
    unittest.main()
