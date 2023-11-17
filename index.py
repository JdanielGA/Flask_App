from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from src.models.user import User

# Desc: Creating the app and defining the routes
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
loging = LoginManager(app)
loging.login_view = 'login'

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == "__main__":
    app.run(debug=True)
