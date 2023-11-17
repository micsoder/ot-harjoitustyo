import unittest
from logic.user_handler import UserHandler
from tests.test_utility.test_database import TestDataBase


class TestUserHandler(unittest.TestCase):

    def setUp(self):
        print('Testing starting...')
        self.test_database = TestDataBase()
        self.user_handler = UserHandler(self.test_database)
        self.user_handler.create_account('Frodo', '123')

    
    def test_create_account_correct_input(self):

        self.user_handler.create_account('Gandalf', '123')
        user = self.test_database.cursor.execute("SELECT username FROM users WHERE username = 'Gandalf'")
        user_result = user.fetchone()
        self.assertEqual(user_result[0], 'Gandalf')

    
    def test_create_account_username_exists(self):

        result = self.user_handler.create_account('Frodo', '456')
        self.assertEqual(result, ('Error', 'Username already exists.'))


    def test_create_account_missing_username(self):

        result = self.user_handler.create_account('', '123')
        self.assertEqual(result, ('Error', 'Enter all information.'))


    def test_create_account_missing_password(self):

        result = self.user_handler.create_account('Frodo', '')
        self.assertEqual(result, ('Error', 'Enter all information.'))


    def test_create_account_missing_username_and_password(self):

        result = self.user_handler.create_account('', '')
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


    def test_login_wrong_password(self):

        result = self.user_handler.login('Frodo', 'wrongpassword')
        self.assertEqual(result, ('Error', 'Invalid password.'))


    def test_login_wrong_username_and_password(self):

        result = self.user_handler.login('NonExistentUser', 'wrongpassword')
        self.assertEqual(result, ('Error', 'Invalid username.'))

