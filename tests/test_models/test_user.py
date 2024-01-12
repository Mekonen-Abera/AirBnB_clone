import os
import models
import unittest
from datetime import datetime
from models.user import User


class TestUserInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_no_args_instantiates(self):
        """Test if User class can be instantiated with no arguments."""
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        """Test if a new instance of User is stored in the objects."""
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test if the id attribute of User is of type str."""
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        """Test if the created_at attribute of User is of type datetime."""
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test if the updated_at attribute of User is of type datetime."""
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        """Test if the email attribute of User is of type str."""
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        """Test if the password attribute of User is of type str."""
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        """Test if the first_name attribute of User is of type str."""
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        """Test if the last_name attribute of User is of type str."""
        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        """Test if two instances of User have unique ids."""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)
    def test_two_users_different_created_at(self):
        """Test if two instances of User have different created_at timestamps."""
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def test_two_users_different_updated_at(self):
        """Test if two instances of User have different updated_at timestamps."""
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_str_representation(self):
        """Test the string representation of User."""
        current_datetime = datetime.today()
        datetime_repr = repr(current_datetime)
        user = User()
        user.id = "123456"
        user.created_at = user.updated_at = current_datetime
        user_str = user.__str__()
        self.assertIn("[User] (123456)", user_str)
        self.assertIn("'id': '123456'", user_str)
        self.assertIn("'created_at': " + datetime_repr, user_str)
        self.assertIn("'updated_at': " + datetime_repr, user_str)

    def test_args_unused(self):
        """Test if the User class instantiation with None does not contain None in its __dict__ values."""
        user = User(None)
        self.assertNotIn(None, user.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test if the User class can be instantiated with specific keyword arguments."""
        current_datetime = datetime.today()
        iso_datetime = current_datetime.isoformat()
        user = User(id="345", created_at=iso_datetime, updated_at=iso_datetime)
        self.assertEqual(user.id, "345")
        self.assertEqual(user.created_at, current_datetime)
        self.assertEqual(user.updated_at, current_datetime)

    def test_instantiation_with_None_kwargs(self):
        """Test if the User class instantiation raises a TypeError when given None as keyword arguments."""
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)
class TestUserSave(unittest.TestCase):
    """Unittests for testing the save method of the User class."""

    @classmethod
    def setUpClass(cls):
        """Set up the test environment by renaming the 'file.json' to 'tmp'."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """Tear down the test environment by removing the 'file.json' and renaming 'tmp' back to 'file.json'."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """Test if the save method updates the 'updated_at' attribute."""
        user = User()
        sleep(0.05)
        first_updated_at = user.updated_at
        user.save()
        self.assertLess(first_updated_at, user.updated_at)

    def test_two_saves(self):
        """Test if the save method updates the 'updated_at' attribute twice."""
        user = User()
        sleep(0.05)
        first_updated_at = user.updated_at
        user.save()
        second_updated_at = user.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        user.save()
        self.assertLess(second_updated_at, user.updated_at)

    def test_save_with_arg(self):
        """Test if the save method raises a TypeError when given an argument."""
        user = User()
        with self.assertRaises(TypeError):
            user.save(None)

    def test_save_updates_file(self):
        """Test if the save method updates the 'file.json' with the User's id."""
        user = User()
        user.save()
        user_id = "User." + user.id
        with open("file.json", "r") as file:
            self.assertIn(user_id, file.read())
class TestUserToDict(unittest.TestCase):
    """Unittests for testing the to_dict method of the User class."""

    def test_to_dict_type(self):
        """Test if the output of to_dict method is of type dict."""
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test if the to_dict method contains the correct keys."""
        user = User()
        self.assertIn("id", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())
        self.assertIn("__class__", user.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test if the to_dict method contains added attributes."""
        user = User()
        user.middle_name = "Holberton"
        user.my_number = 98
        self.assertEqual("Holberton", user.middle_name)
        self.assertIn("my_number", user.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test if the datetime attributes in the to_dict method are of type str."""
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(str, type(user_dict["id"]))
        self.assertEqual(str, type(user_dict["created_at"]))
        self.assertEqual(str, type(user_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test the output of the to_dict method."""
        current_datetime = datetime.today()
        user = User()
        user.id = "123456"
        user.created_at = user.updated_at = current_datetime
        expected_dict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': current_datetime.isoformat(),
            'updated_at': current_datetime.isoformat(),
        }
        self.assertDictEqual(user.to_dict(), expected_dict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test if the output of to_dict method is not equal to the __dict__ attribute."""
        user = User()
        self.assertNotEqual(user.to_dict(), user.__dict__)

    def test_to_dict_with_arg(self):
        """Test if the to_dict method raises a TypeError when given an argument."""
        user = User()
        with self.assertRaises(TypeError):
            user.to_dict(None)

if __name__ == "__main__":
    unittest.main()
