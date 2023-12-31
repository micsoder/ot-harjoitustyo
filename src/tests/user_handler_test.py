import unittest
from logic.user_handler import UserHandler
from tests.test_utility.test_database import TestDataBase


class TestUserHandler(unittest.TestCase):

    def setUp(self):
        print('Testing starting...')
        self.test_database = TestDataBase()
        self.user_handler = UserHandler(self.test_database)
        self.user_handler.create_account('Frodo', '123', 1)
        self.user_handler.create_account('Samwise', '456', 0)

    def test_create_account_correct_input(self):

        self.user_handler.create_account('Gandalf', '123', 1)
        user = self.test_database.cursor.execute(
            "SELECT username FROM users WHERE username = 'Gandalf'")
        user_result = user.fetchone()
        self.assertEqual(user_result[0], 'Gandalf')

    def test_create_account_username_exists(self):

        result = self.user_handler.create_account('Frodo', '456', 1)
        self.assertEqual(
            result, ('Error', 'User with username Frodo exists already'))

    def test_is_bad_password(self):

        result = self.user_handler.create_account('Sauron', '4', 1)
        self.assertEqual(
            result, ('Error', "Password needs to be at least three characters long"))

    def test_create_account_missing_username(self):

        result = self.user_handler.create_account('', '123', 1)
        self.assertEqual(result, ('Error', 'Enter all information.'))

    def test_create_account_missing_password(self):

        result = self.user_handler.create_account('Frodo', '', 1)
        self.assertEqual(result, ('Error', 'Enter all information.'))

    def test_create_account_missing_username_and_password(self):

        result = self.user_handler.create_account('', '', 0)
        self.assertEqual(result, ('Error', 'Enter all information.'))

    def test_login_correct_input(self):

        result = self.user_handler.login('Frodo', '123')
        self.assertEqual(result, ('Success', 'Logged in successfully.'))

    def test_login_wrong_password(self):

        result = self.user_handler.login('Frodo', '000')
        self.assertEqual(result, ('Error', 'Invalid password.'))

    def test_login_missing_username(self):

        result = self.user_handler.login('', '000')
        self.assertEqual(result, ('Error', 'Enter all information.'))

    def test_login_missing_password(self):

        result = self.user_handler.login('Frodo', '')
        self.assertEqual(result, ('Error', 'Enter all information.'))

    def test_login_wrong_username(self):

        result = self.user_handler.login('NonExistentUser', '000')
        self.assertEqual(result, ('Error', 'Invalid username.'))

    def test_login_wrong_username_and_password(self):

        result = self.user_handler.login('NonExistentUser', 'wrongpassword')
        self.assertEqual(result, ('Error', 'Invalid username.'))

    def test_is_admin_true(self):
        self.user_handler.login('Frodo', '123')
        result = self.user_handler.is_admin()
        self.assertTrue(result)

    def test_is_admin_false(self):
        self.user_handler.login('Samwise', '456')
        result = self.user_handler.is_admin()
        self.assertFalse(result)
