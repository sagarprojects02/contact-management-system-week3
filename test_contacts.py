import unittest
from contacts_manager import validate_phone, validate_name

class TestContacts(unittest.TestCase):

    def test_valid_phone(self):
        self.assertTrue(validate_phone("9876543210"))

    def test_invalid_phone(self):
        self.assertFalse(validate_phone("12345"))

    def test_valid_name(self):
        self.assertTrue(validate_name("Sagar Yadav"))

    def test_invalid_name(self):
        self.assertFalse(validate_name("Sagar123"))

if __name__ == "__main__":
    unittest.main()
