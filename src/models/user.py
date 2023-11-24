''' User model. '''
# Route "src/models/user.py".
# Desc: Modules and libraries for users model.
from config.config import db
from flask_security import UserMixin, RoleMixin, AsaList
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.mutable import MutableList

# Desc: Class table for the relationship between users and roles.
class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer(), primary_key=True, index=True, nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id'), nullable=False)

# Desc: Class table for the roles model.
class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True, index=True, nullable=False)
    name = db.Column(db.String(80), unique=True, index=True, nullable=False)
    description = db.Column(db.String(255))
    permissions = db.Column(MutableList.as_mutable(AsaList()), nullable=True)
    role = db.relationship('User', secondary='roles_users', backref=db.backref('users', lazy='dynamic'))

    # Desc: Method to print the object.
    def __repr__(self):
        return '<Role %r>' % self.name


# Desc: Class for the users model.
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, index=True, nullable=False)
    username = db.Column(db.String(50), unique=True, index=True, nullable=False)
    email = db.Column(db.String(50), unique=True, index=True, nullable=False)
    _password = db.Column('password', db.String(255), nullable=False)
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True)
    roles = db.relationship('Role', secondary='roles_users', backref=db.backref('users', lazy='dynamic'))

    # Desc: Property to get the password.
    @property
    def password(self):
        return self._password
    
    # Desc: Property to set the password.
    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    # Desc: Method to check a password hash.
    def check_password(self, password):
        return check_password_hash(self._password, password)
    
    # Desc: Method to print the object.
    def __repr__(self):
        return '<User %r>' % self.username