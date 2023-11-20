''' Login test. '''
# Desc: Modules and libraries for the test.
import unittest
from flask import Flask
from config.config import Config, db
from src.models.user import User


# Desc: User data.
username = 'admin'
email = 'admin@localhost.com'
password = 'admin'

# Desc: Login function.
def login(username, email, password):
    # Desc: Check if the username or email was entered.
    if not username and not email:
        return False
    # Desc: Check if the username or email exists.
    user = User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first()
    if not user:
        return False
    # Desc: Check if the password is correct.
    if not user.check_password(password):
        return False
    return True

# Desc: Test class.
class LoginTest(unittest.TestCase):
    # Desc: Setup function.
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config.from_object(Config)
        db.init_app(self.app)
        self.app_context = self.app.app_context()
        self.app_context.push()

    # Desc: Test login function.
    def test_login(self):
        # Test with correct username and password.
        self.assertTrue(login(username, None, password))
        print('\n1) - Test with correct username and password passed successfully.')

        # Test with incorrect username.
        self.assertFalse(login('wrong_username', None, password))
        print('2) - Test with incorrect username passed successfully.')

        # Test with incorrect password.
        self.assertFalse(login(username, None, 'wrong_password'))
        print('3) - Test with incorrect password passed successfully.')

        # Test with correct email and password.
        self.assertTrue(login(None, email, password))
        print('4) - Test with correct email and password passed successfully.')

        # Test with incorrect email.
        self.assertFalse(login(None, 'wrong_email', password))
        print('5) - Test with incorrect email passed successfully.')

        # Test with incorrect password.
        self.assertFalse(login(None, email, 'wrong_password'))
        print('6) - Test with incorrect password passed successfully.')

        # Desc: Print the result.
        print('\nLogin test passed successfully!')

if __name__ == "__main__":
    unittest.main()
