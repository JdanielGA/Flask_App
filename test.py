# Desc: Modules and libraries to perform user creation tests.
import unittest
from flask import Flask
from flask_security import Security, SQLAlchemySessionUserDatastore

# Desc: My own modules and libraries to perform user creation tests.
from config.config import db, Config
from src.models.user import User, Role

# Desc: Class to perform user creation tests.
class UserModelTest(unittest.TestCase):

    # Desc: Method to set up the test.
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config.from_object(Config)
        self.db = db
        self.db.init_app(self.app)

        with self.app.app_context():
            self.db.create_all()

    # Desc: Method to test the password setter.
    def test_password_setter(self):
        u = User(username='john', email='john@example.com')
        u.generate_password('cat')
        self.assertTrue(u._password is not None)

    # Desc: Method to test the password getter.
    def test_no_password_getter(self):
        u = User(username='john', email='john@example.com')
        with self.assertRaises(AttributeError):
            u.password

    # Desc: Method to test the password verification.
    def test_password_verification(self):
        u = User(username='john', email='john@example.com')
        u.generate_password('cat')
        self.assertTrue(u.check_password('cat'))
        self.assertFalse(u.check_password('dog'))

    # Desc: Method to test the password salting.
    def test_password_salts_are_random(self):
        u = User(username='john', email='john@example.com')
        u.generate_password('cat')
        u2 = User(username='susan', email='susan@example.com')
        u2.generate_password('cat')
        self.assertTrue(u._password != u2._password)

    # Desc: Method to test the user creation.
    def tearDown(self):
        with self.app.app_context():
            self.db.session.remove()
            self.db.drop_all()

if __name__ == '__main__':
    unittest.main()