''' User services '''
## Route "src/services/user.py" file.
# Desc: Modules and libraries for user services.
from config.config import db
from src.models.user import User

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
    return True
