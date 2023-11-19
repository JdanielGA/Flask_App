# Desc: Modules and libraries for login model.
from wtforms import StringField, PasswordField, SubmitField, validators
from flask_wtf import FlaskForm

# Desc: Class for login model.
class LoginForm(FlaskForm):
    username = StringField('Username:', [validators.DataRequired()])
    password = PasswordField('Password:', [validators.DataRequired()])
    login = SubmitField('Login')