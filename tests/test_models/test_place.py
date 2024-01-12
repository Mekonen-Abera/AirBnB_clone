#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlaceInstantiation
    TestPlaceSave
    TestPlaceToDict
"""
import os
import models
import unittest
from datetime import datetime
from models.place import Place

class TestPlaceInstantiation(unittest.TestCase):
    """Test cases for the instantiation of the Place class."""

    def test_no_args_instantiates(self):
        """Test if Place can be instantiated with no arguments."""
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        """Test if a new instance of Place is stored in the objects attribute of the storage module."""
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test if the id attribute of Place is of type str."""
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        """Test if the created_at attribute of Place is of type datetime."""
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test if the updated_at attribute of Place is of type datetime."""
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        """Test if city_id is a public class attribute of Place."""
        place = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(place))
        self.assertNotIn("city_id", place.__dict__)

    def test_user_id_is_public_class_attribute(self):
        """Test if user_id is a public class attribute of Place."""
        place = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(place))
        self.assertNotIn("user_id", place.__dict__)
 def test_name_is_public_class_attribute(self):
        """Test if name is a public class attribute of Place."""
        place = Place()
        self.assertEqual(str, type(place.name))
        self.assertIn("name", dir(place))
        self.assertNotIn("name", place.__dict__)

    def test_description_is_public_class_attribute(self):
        """Test if description is a public class attribute of Place."""
        place = Place()
        self.assertEqual(str, type(place.description))
        self.assertIn("description", dir(place))
        self.assertNotIn("description", place.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        """Test if number_rooms is a public class attribute of Place."""
        place = Place()
        self.assertEqual(int, type(place.number_rooms))
        self.assertIn("number_rooms", dir(place))
        self.assertNotIn("number_rooms", place.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        """Test if number_bathrooms is a public class attribute of Place."""
        place = Place()
        self.assertEqual(int, type(place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(place))
        self.assertNotIn("number_bathrooms", place.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        """Test if max_guest is a public class attribute of Place."""
        place = Place()
        self.assertEqual(int, type(place.max_guest))
        self.assertIn("max_guest", dir(place))
        self.assertNotIn("max_guest", place.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        """Test if price_by_night is a public class attribute of Place."""
        place = Place()
        self.assertEqual(int, type(place.price_by_night))
        self.assertIn("price_by_night", dir(place))
        self.assertNotIn("price_by_night", place.__dict__)

    def test_latitude_is_public_class_attribute(self):
        """Test if latitude is a public class attribute of Place."""
        place = Place()
        self.assertEqual(float, type(place.latitude))
        self.assertIn("latitude", dir(place))
        self.assertNotIn("latitude", place.__dict__)

    def test_longitude_is_public_class_attribute(self):
        """Test if longitude is a public class attribute of Place."""
        place = Place()
        self.assertEqual(float, type(place.longitude))
        self.assertIn("longitude", dir(place))
        self.assertNotIn("longitude", place.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        """Test if amenity_ids is a public class attribute of Place."""
        place = Place()
        self.assertEqual(list, type(place.amenity_ids))
        self.assertIn("amenity_ids", dir(place))
        self.assertNotIn("amenity_ids", place.__dict__)
        def test_two_places_unique_ids(self):
        """Test if two instances of Place have unique ids."""
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_two_places_different_created_at(self):
        """Test if two instances of Place have different created_at timestamps."""
        place1 = Place()
        sleep(0.05)
        place2 = Place()
        self.assertLess(place1.created_at, place2.created_at)

    def test_two_places_different_updated_at(self):
        """Test if two instances of Place have different updated_at timestamps."""
        place1 = Place()
        sleep(0.05)
        place2 = Place()
        self.assertLess(place1.updated_at, place2.updated_at)

    def test_str_representation(self):
        """Test the string representation of Place."""
        current_datetime = datetime.today()
        dt_repr = repr(current_datetime)
        place = Place()
        place.id = "123456"
        place.created_at = place.updated_at = current_datetime
        place_str = place.__str__()
        self.assertIn("[Place] (123456)", place_str)
        self.assertIn("'id': '123456'", place_str)
        self.assertIn("'created_at': " + dt_repr, place_str)
        self.assertIn("'updated_at': " + dt_repr, place_str)

    def test_args_unused(self):
        """Test if instantiation with None does not add any attributes to the instance."""
        place = Place(None)
        self.assertNotIn(None, place.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test instantiation of Place with keyword arguments."""
        current_datetime = datetime.today()
        dt_iso = current_datetime.isoformat()
        place = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(place.id, "345")
        self.assertEqual(place.created_at, current_datetime)
        self.assertEqual(place.updated_at, current_datetime)

    def test_instantiation_with_None_kwargs(self):
        """Test if instantiation with None keyword arguments raises a TypeError."""
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)
            class TestPlaceSave(unittest.TestCase):
    """Unittests for testing the save method of the Place class."""

    @classmethod
    def setUpClass(cls):
        """Set up the test class by renaming the 'file.json' to 'tmp'."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        """Tear down the test class by removing 'file.json' and renaming 'tmp' back to 'file.json'."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """Test if the save method updates the 'updated_at' attribute of Place."""
        place = Place()
        sleep(0.05)
        first_updated_at = place.updated_at
        place.save()
        self.assertLess(first_updated_at, place.updated_at)

    def test_two_saves(self):
        """Test if consecutive saves update the 'updated_at' attribute of Place."""
        place = Place()
        sleep(0.05)
        first_updated_at = place.updated_at
        place.save()
        second_updated_at = place.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        place.save()
        self.assertLess(second_updated_at, place.updated_at)

    def test_save_with_arg(self):
        """Test if the save method raises a TypeError when passed an argument."""
        place = Place()
        with self.assertRaises(TypeError):
            place.save(None)

    def test_save_updates_file(self):
        """Test if the save method updates the 'file.json' with the new Place instance."""
        place = Place()
        place.save()
        place_id = "Place." + place.id
        with open("file.json", "r") as file:
            self.assertIn(place_id, file.read())


class TestPlaceToDict(unittest.TestCase):
    """Unittests for testing the to_dict method of the Place class."""

    def test_to_dict_type(self):
        """Test if the output of to_dict method is of type dict."""
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test if the output of to_dict method contains the correct keys."""
        place = Place()
        self.assertIn("id", place.to_dict())
        self.assertIn("created_at", place.to_dict())
        self.assertIn("updated_at", place.to_dict())
        self.assertIn("__class__", place.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test if the output of to_dict method contains added attributes."""
        place = Place()
        place.middle_name = "Holberton"
        place.my_number = 98
        self.assertEqual("Holberton", place.middle_name)
        self.assertIn("my_number", place.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test if the datetime attributes in the output of to_dict method are of type str."""
        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(str, type(place_dict["id"]))
        self.assertEqual(str, type(place_dict["created_at"]))
        self.assertEqual(str, type(place_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test the output of to_dict method with specific attribute values."""
        current_datetime = datetime.today()
        place = Place()
        place.id = "123456"
        place.created_at = place.updated_at = current_datetime
        expected_dict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': current_datetime.isoformat(),
            'updated_at': current_datetime.isoformat(),
        }
        self.assertDictEqual(place.to_dict(), expected_dict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test if the output of to_dict method is not equal to the __dict__ attribute."""
        place = Place()
        self.assertNotEqual(place.to_dict(), place.__dict__)

    def test_to_dict_with_arg(self):
        """Test if the to_dict method raises a TypeError when passed an argument."""
        place = Place()
        with self.assertRaises(TypeError):
            place.to_dict(None)


if __name__ == "__main__":
    unittest.main()

