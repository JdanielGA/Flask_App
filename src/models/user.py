# Desc: Libraries for user model
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

# Create user instance from SQLAlchemy class
db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        # Generate password hash for new users
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # Check password hash for existing users
        return check_password_hash(self.password_hash, password)