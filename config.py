class Config(object):
    SECRET_KEY = 'tu-clave-secreta'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///src/database/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False