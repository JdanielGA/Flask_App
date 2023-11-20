# Desc: Modules and libraries for login route.
from flask import Blueprint, render_template, request, redirect, url_for, flash

# Desc: My own modules and libraries for login route.
from src.models.login import LoginForm

# Desc: Blueprint for login route.
auth_blueprint = Blueprint('login', __name__)

# Desc: Login route.
@auth_blueprint.route('/')
@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('Successful login message')
        return redirect(url_for('home.home'))
    else:
        flash('Invalid username or password')
    return render_template('pages/login.html', form=form)