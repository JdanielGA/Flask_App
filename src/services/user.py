''' User services '''
## Path: "src/services/user.py".
# Desc: Modules and libraries for user services.
import uuid
# Desc: My own modules and libraries for user services.
from config.config import db
from src.models.user import User, Role, RolesUsers

# Desc: Funtion to login user.
def login_user(username=None, password=None):

    # Desc: Check if the user name is username or email.
    user = User.query.filter_by(username=username).first()
    if not user:
        user = User.query.filter_by(email=username).first()
        if not user:
            return False
    if not user.check_password(password):
        return False
    # Desc: return id and username.
    return user.id, user.username

# Desc: Funtion to create a new user.
def create_user(id=None, username=None, email=None, password=None, password_confirmation=None,active=True, roles=None):
    
    # Desc: Check if id already exists.
    user = User.query.filter_by(id=id).first()
    if user:
        return ('User id already exists in the database!', 'error')
    # Desc: Check if username already exists.
    user = User.query.filter_by(username=username).first()
    if user:
        return ('Username already exists in the database!', 'error')
    # Desc: Check if email already exists.
    user = User.query.filter_by(email=email).first()
    if user:
        return ('Email already exists in the database!', 'error')
    # Desc: Check if roles exists.
    user_role = Role.query.filter_by(name=roles).first()
    if user_role is None:
        return ('Role does not exist!', 'error')
    # Desc: Create the user.
    user = User(
        id=id,
        username=username,
        email=email,
        fs_uniquifier=str(uuid.uuid4()),
        active=active,
        roles=[user_role])
    # Desc: Check if password and password_confirmation are the same.
    if password != password_confirmation:
        return ('Password and password confirmation are not the same!', 'error')
    user.password = password
    db.session.add(user)
    db.session.commit()

    # Desc: Assign role to user.
    role_user = RolesUsers(
        user_id=user.id,
        role_id=user_role.id)
    db.session.add(role_user)
    db.session.commit()
    return ('User created successfully!', 'success')