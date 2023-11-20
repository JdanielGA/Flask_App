# Desc: Modules and libraries to perform login tests.
import unittest
from flask import Flask
from flask_security import Security, SQLAlchemyUserDatastore, login_user, current_user

# Desc: My own modules and libraries to perform login tests.
from config.config import db, Config
from src.models.user import User, Role

# Desc: Class to perform login tests.
class LoginTest(unittest.TestCase):
    def setUp(self):
        # Desc: Create application.
        self.app = Flask(__name__)
        self.app.config.from_object(Config)
        Config.init_app(self.app)
        self.client = self.app.test_client()
        self.ctx = self.app.test_request_context()
        self.ctx.push()

        # Desc: Create database.
        with self.app.app_context():
            db.create_all()

        # Desc: Initialize Flask-Security
        self.user_datastore = SQLAlchemyUserDatastore(db, User, Role)
        self.security = Security(self.app, self.user_datastore)

        # Desc: Create a user for the tests.
        self.test_user = self.user_datastore.create_user(
            username='testuser',
            email='test@example.com',
            password='password'
        )
        db.session.commit()


    def tearDown(self):
        # Desc: Delete test request context.
        self.ctx.pop()


    def test_login(self):
        # Desc: Test login with the test user.
        with self.client:
            login_user(self.test_user)
            self.assertTrue(current_user.is_authenticated)

if __name__ == '__main__':
    unittest.main()
