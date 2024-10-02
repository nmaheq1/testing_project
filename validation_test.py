import unittest
from unittest.mock import patch, MagicMock
from Validation import validation  # Update 'your_module' with the actual name of your module

class TestValidation(unittest.TestCase):

    def setUp(self):
        """Create a validation instance before each test."""
        self.validator = validation()

    @patch.object(validation.Database, 'getUsername')
    def test_check_username_valid(self, mock_getUsername):
        """Test valid username."""
        mock_getUsername.return_value = ['existingUser1', 'existingUser2']
        result = self.validator.checkUsername('newUser')
        self.assertEqual(result, (0, "no error"))

    @patch.object(validation.Database, 'getUsername')
    def test_check_username_too_short(self, mock_getUsername):
        """Test username that's too short."""
        mock_getUsername.return_value = []
        result = self.validator.checkUsername('ab')
        self.assertEqual(result, (1, "Username must be between 3 and 17 characters"))

    @patch.object(validation.Database, 'getUsername')
    def test_check_username_exists(self, mock_getUsername):
        """Test username that already exists."""
        mock_getUsername.return_value = ['existingUser', 'newUser']
        result = self.validator.checkUsername('existingUser')
        self.assertEqual(result, (1, "Username already exists"))

    def test_check_password_valid(self):
        """Test valid password."""
        result = self.validator.checkPassword('Valid123')
        self.assertEqual(result, (0, "no error"))

    def test_check_password_too_short(self):
        """Test password that's too short."""
        result = self.validator.checkPassword('Short1')
        self.assertEqual(result, (1, "Password must be between 8 and 17 characters"))

    def test_check_password_no_uppercase(self):
        """Test password missing uppercase letter."""
        result = self.validator.checkPassword('invalidpassword1')
        self.assertEqual(result, (1, "Password must contain an Uppercase letter"))

    def test_check_password_no_lowercase(self):
        """Test password missing lowercase letter."""
        result = self.validator.checkPassword('INVALIDPASSWORD1')
        self.assertEqual(result, (1, "Password must contain a lowercase letter"))

    def test_check_password_no_number(self):
        """Test password missing number."""
        result = self.validator.checkPassword('InvalidPassword')
        self.assertEqual(result, (1, "Password must contain a number"))

    def test_check_entries_valid(self):
        """Test valid entries."""
        entries = [MagicMock(get=lambda: 'valid entry'), MagicMock(get=lambda: 'another valid entry')]
        result = self.validator.checkEntries(entries)
        self.assertEqual(result, 0)

    def test_check_entries_empty(self):
        """Test empty entry."""
        entries = [MagicMock(get=lambda: ''), MagicMock(get=lambda: 'valid entry')]
        result = self.validator.checkEntries(entries)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
