''' Flask-Security '''
# Desc: Modules and libraries for authentication services.
from config.config import db
from flask_security import Security, SQLAlchemyUserDatastore
# Desc: My own modules and libraries for authentication services.
from src.models.user import User, Role

# Desc: Initialize Flask-Security.
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = None

# Desc: Function to initialize Flask-Security.
def init_security(app):
    global security
    security = Security(app, user_datastore)