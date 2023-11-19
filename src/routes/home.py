# Desc: Modules and libraries for home route
from flask import Blueprint, render_template

# Desc: Blueprint for home route
home_blueprint = Blueprint('home', __name__)   

# Desc: Home route
@home_blueprint.route('/')
@home_blueprint.route('/home')
def home():
    return render_template('pages/home.html')