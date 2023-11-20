''' Login test. '''
# Desc: Modules and libraries for the test.
import unittest
from flask import Flask
from config.config import Config, db
from src.models.user import User


# Desc: User data.
username = 'admin'
password = 'admin'

# Desc: Login function.
def login(username, password):
    # Desc: Check if the user exists.
    user = db.session.query(User).filter_by(username=username).first()
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
        self.assertTrue(login(username, password))
        print('\n1) - Test with correct username and password passed successfully.')

        # Test with incorrect username.
        self.assertFalse(login('wrong_username', password))
        print('2) - Test with incorrect username passed successfully.')

        # Test with incorrect password.
        self.assertFalse(login(username, 'wrong_password'))
        print('3) - Test with incorrect password passed successfully.')

        # Desc: Print the result.
        print('\nLogin test passed successfully!')

if __name__ == "__main__":
    unittest.main()
