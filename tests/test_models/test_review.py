#!/usr/bin/python3
"""Defines unittests for models/review.py.

Unittest classes:
    TestReviewInstantiation
    TestReviewSave
    TestReviewToDict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReviewInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_no_args_instantiates(self):
        """Test if Review can be instantiated with no arguments."""
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        """Test if a new instance of Review is stored in the objects attribute of the storage module."""
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test if the id attribute of Review is of type str."""
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        """Test if the created_at attribute of Review is of type datetime."""
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test if the updated_at attribute of Review is of type datetime."""
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        """Test if place_id is a public class attribute of Review."""
        review = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(review))
        self.assertNotIn("place_id", review.__dict__)

    def test_user_id_is_public_class_attribute(self):
        """Test if user_id is a public class attribute of Review."""
        review = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(review))
        self.assertNotIn("user_id", review.__dict__)

    def test_text_is_public_class_attribute(self):
        """Test if text is a public class attribute of Review."""
        review = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(review))
        self.assertNotIn("text", review.__dict__)

    def test_two_reviews_unique_ids(self):
        """Test if two instances of Review have unique ids."""
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_two_reviews_different_created_at(self):
        """Test if two instances of Review have different created_at timestamps."""
        review1 = Review()
        sleep(0.05)
        review2 = Review()
        self.assertLess(review1.created_at, review2.created_at)

    def test_two_reviews_different_updated_at(self):
        """Test if two instances of Review have different updated_at timestamps."""
        review1 = Review()
        sleep(0.05)
        review2 = Review()
        self.assertLess(review1.updated_at, review2.updated_at)

    def test_str_representation(self):
        """Test the string representation of Review."""
        current_datetime = datetime.today()
        dt_repr = repr(current_datetime)
        review = Review()
        review.id = "123456"
        review.created_at = review.updated_at = current_datetime
        review_str = review.__str__()
        self.assertIn("[Review] (123456)", review_str)
        self.assertIn("'id': '123456'", review_str)
        self.assertIn("'created_at': " + dt_repr, review_str)
        self.assertIn("'updated_at': " + dt_repr, review_str)

    def test_args_unused(self):
        """Test if instantiation with None does not add any attributes to the instance."""
        review = Review(None)
        self.assertNotIn(None, review.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test instantiation of Review with keyword arguments."""
        current_datetime = datetime.today()
        dt_iso = current_datetime.isoformat()
        review = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(review.id, "345")
        self.assertEqual(review.created_at, current_datetime)
        self.assertEqual(review.updated_at, current_datetime)

    def test_instantiation_with_None_kwargs(self):
        """Test if instantiation with None keyword arguments raises a TypeError."""
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)
class TestReviewSave(unittest.TestCase):
    """Unittests for testing the save method of the Review class."""

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
        """Test if the save method updates the 'updated_at' attribute of Review."""
        review = Review()
        sleep(0.05)
        first_updated_at = review.updated_at
        review.save()
        self.assertLess(first_updated_at, review.updated_at)

    def test_two_saves(self):
        """Test if consecutive saves update the 'updated_at' attribute of Review."""
        review = Review()
        sleep(0.05)
        first_updated_at = review.updated_at
        review.save()
        second_updated_at = review.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        review.save()
        self.assertLess(second_updated_at, review.updated_at)

    def test_save_with_arg(self):
        """Test if the save method raises a TypeError when passed an argument."""
        review = Review()
        with self.assertRaises(TypeError):
            review.save(None)

    def test_save_updates_file(self):
        """Test if the save method updates the 'file.json' with the new Review instance."""
        review = Review()
        review.save()
        review_id = "Review." + review.id
        with open("file.json", "r") as file:
            self.assertIn(review_id, file.read())


class TestReviewToDict(unittest.TestCase):
    """Unittests for testing the to_dict method of the Review class."""

    def test_to_dict_type(self):
        """Test if the output of to_dict method is of type dict."""
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test if the output of to_dict method contains the correct keys."""
        review = Review()
        self.assertIn("id", review.to_dict())
        self.assertIn("created_at", review.to_dict())
        self.assertIn("updated_at", review.to_dict())
        self.assertIn("__class__", review.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test if the output of to_dict method contains added attributes."""
        review = Review()
        review.middle_name = "Holberton"
        review.my_number = 98
        self.assertEqual("Holberton", review.middle_name)
        self.assertIn("my_number", review.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test if the datetime attributes in the output of to_dict method are of type str."""
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(str, type(review_dict["id"]))
        self.assertEqual(str, type(review_dict["created_at"]))
        self.assertEqual(str, type(review_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test the output of to_dict method with specific attribute values."""
        current_datetime = datetime.today()
        review = Review()
        review.id = "123456"
        review.created_at = review.updated_at = current_datetime
        expected_dict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': current_datetime.isoformat(),
            'updated_at': current_datetime.isoformat(),
        }
        self.assertDictEqual(review.to_dict(), expected_dict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test if the output of to_dict method is not equal to the __dict__ attribute."""
        review = Review()
        self.assertNotEqual(review.to_dict(), review.__dict__)

    def test_to_dict_with_arg(self):
        """Test if the to_dict method raises a TypeError when passed an argument."""
        review = Review()
        with self.assertRaises(TypeError):
            review.to_dict(None)


if __name__ == "__main__":
    unittest.main()

