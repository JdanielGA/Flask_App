''' Client model. '''
## Path: "src/models/clients.py".
# Desc: Modules and libraries for clients model.
from config.config import db
from flask_security import UserMixin
# Desc: Modules and libraries for clients form.
from wtforms import StringField, SubmitField, validators
from flask_wtf import FlaskForm

# Desc: Client model class.
class Client(db.Model, UserMixin):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nit = db.Column(db.String(50), unique=True, index=True, nullable=False)
    name = db.Column(db.String(50), unique=True, index=True, nullable=False)
    lastname = db.Column(db.String(50), unique=True, index=True, nullable=True)
    email = db.Column(db.String(50), unique=True, index=True, nullable=False)
    phone = db.Column(db.String(50), unique=True, index=True, nullable=False)
    address = db.Column(db.String(50), unique=True, index=True, nullable=True)
    city = db.Column(db.String(50), unique=True, index=True, nullable=True)
    state = db.Column(db.String(50), unique=True, index=True, nullable=True)
    notes = db.Column(db.String(255), unique=True, index=True, nullable=True)

    # Desc: Method to print the object.
    def __repr__(self):
        return '<Client %r>' % self.name
    
# Desc: Client form class.
class ClientForm(FlaskForm):
    nit = StringField('Nit:', [validators.DataRequired()])
    name = StringField('Name:', [validators.DataRequired()])
    lastname = StringField('Lastname:', [validators.DataRequired()])
    email = StringField('Email:', [validators.DataRequired()])
    phone = StringField('Phone:', [validators.DataRequired()])
    address = StringField('Address:', [validators.DataRequired()])
    city = StringField('City:', [validators.DataRequired()])
    state = StringField('State:', [validators.DataRequired()])
    notes = StringField('Notes:', [validators.DataRequired()])
    register = SubmitField('Register')
    update = SubmitField('Update')