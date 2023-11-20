# Desc: Modules and libraries to config the app.
from flask_sqlalchemy import SQLAlchemy
import os

# Desc: Database name in the path (if it doesn't exist, it will be created).
database_name = '../src/database/database.sqlite'

# Desc: Directory where the database is located.
project_dir = os.path.dirname(os.path.abspath(__file__))

# Desc: Database URL.
database_url = f'sqlite:///{os.path.join(project_dir, database_name)}'

# Desc: SQLAlchemy instance
db = SQLAlchemy()

# Desc: Object config.
class Config(object):
    SECRET_KEY = 'tu-clave-secreta'
    SQLALCHEMY_DATABASE_URI = database_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        db.init_app(app)
