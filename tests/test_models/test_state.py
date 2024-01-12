#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestStateInstantiation
    TestStateSave
    TestStateToDict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestStateInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

    def test_no_args_instantiates(self):
        """Test if State can be instantiated with no arguments."""
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objects(self):
        """Test if a new instance of State is stored in the objects attribute of the storage module."""
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test if the id attribute of State is of type str."""
        self.assertEqual(str, type(State().id))

    def test_created_at_is_public_datetime(self):
        """Test if the created_at attribute of State is of type datetime."""
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test if the updated_at attribute of State is of type datetime."""
        self.assertEqual(datetime, type(State().updated_at))

    def test_name_is_public_class_attribute(self):
        """Test if name is a public class attribute of State."""
        state = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(state))
        self.assertNotIn("name", state.__dict__)

    def test_two_states_unique_ids(self):
        """Test if two instances of State have unique ids."""
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_two_states_different_created_at(self):
        """Test if two instances of State have different created_at timestamps."""
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.created_at, state2.created_at)

    def test_two_states_different_updated_at(self):
        """Test if two instances of State have different updated_at timestamps."""
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.updated_at, state2.updated_at)

    def test_str_representation(self):
        """Test the string representation of State."""
        current_datetime = datetime.today()
        dt_repr = repr(current_datetime)
        state = State()
        state.id = "123456"
        state.created_at = state.updated_at = current_datetime
        state_str = state.__str__()
        self.assertIn("[State] (123456)", state_str)
        self.assertIn("'id': '123456'", state_str)
        self.assertIn("'created_at': " + dt_repr, state_str)
        self.assertIn("'updated_at': " + dt_repr, state_str)

    def test_args_unused(self):
        """Test if instantiation with None does not add any attributes to the instance."""
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test instantiation of State with keyword arguments."""
        current_datetime = datetime.today()
        dt_iso = current_datetime.isoformat()
        state = State(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(state.id, "345")
        self.assertEqual(state.created_at, current_datetime)
        self.assertEqual(state.updated_at, current_datetime)

    def test_instantiation_with_None_kwargs(self):
        """Test if instantiation with None keyword arguments raises a TypeError."""
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestStateSave(unittest.TestCase):
    """Unittests for testing the save method of the State class."""

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
        """Test if the save method updates the 'updated_at' attribute of State."""
        state = State()
        sleep(0.05)
        first_updated_at = state.updated_at
        state.save()
        self.assertLess(first_updated_at, state.updated_at)
            def test_two_saves(self):
        st = State()
        sleep(0.05)
        first_updated_at = st.updated_at
        st.save()
        second_updated_at = st.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        st.save()
        self.assertLess(second_updated_at, st.updated_at)

    def test_save_with_arg(self):
        st = State()
        with self.assertRaises(TypeError):
            st.save(None)

    def test_save_updates_file(self):
        st = State()
        st.save()
        stid = "State." + st.id
        with open("file.json", "r") as f:
            self.assertIn(stid, f.read())
class TestStateToDict(unittest.TestCase):
    """Unittests for testing the to_dict method of the State class."""

    def test_to_dict_type(self):
        """Test if the to_dict method returns a dictionary."""
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test if the to_dict method contains the correct keys."""
        state = State()
        self.assertIn("id", state.to_dict())
        self.assertIn("created_at", state.to_dict())
        self.assertIn("updated_at", state.to_dict())
        self.assertIn("__class__", state.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test if the to_dict method contains added attributes."""
        state = State()
        state.middle_name = "Holberton"
        state.my_number = 98
        self.assertEqual("Holberton", state.middle_name)
        self.assertIn("my_number", state.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test if the datetime attributes in the to_dict method are of type str."""
        state = State()
        state_dict = state.to_dict()
        self.assertEqual(str, type(state_dict["id"]))
        self.assertEqual(str, type(state_dict["created_at"]))
        self.assertEqual(str, type(state_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test the output of the to_dict method."""
        current_datetime = datetime.today()
        state = State()
        state.id = "123456"
        state.created_at = state.updated_at = current_datetime
        expected_dict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': current_datetime.isoformat(),
            'updated_at': current_datetime.isoformat(),
        }
        self.assertDictEqual(state.to_dict(), expected_dict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test the contrast between the to_dict method and the __dict__ attribute."""
        state = State()
        self.assertNotEqual(state.to_dict(), state.__dict__)

    def test_to_dict_with_arg(self):
        """Test if the to_dict method raises a TypeError when given an argument."""
        state = State()
        with self.assertRaises(TypeError):
            state.to_dict(None)
        state = State()
        with self.assertRaises(TypeError):
            state.to_dict(None)


if __name__ == "__main__":
    unittest.main()

