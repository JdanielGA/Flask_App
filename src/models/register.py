''' Registration model '''
## Path: "src/models/register.py".
# Desc: Modules and libraries for register model.
from wtforms import StringField, PasswordField, SubmitField, validators, SelectField
from flask_wtf import FlaskForm

# Desc: Class for register model.
class RegisterForm(FlaskForm):
    id = StringField('Id:', [validators.DataRequired()])
    username = StringField('Username:', [validators.DataRequired()])
    email = StringField('Email:', [validators.DataRequired()])
    password = PasswordField('Password:', [validators.DataRequired()])
    password_confirmation = PasswordField('Confirm Password:', [validators.DataRequired()])
    roles = SelectField('Role:', choices=[('user', 'User'), ('guest', 'Guest')], validators=[validators.DataRequired()])
    register = SubmitField('Register')
