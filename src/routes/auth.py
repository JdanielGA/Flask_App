''' Aunthentication route '''
## Route "src/routes/auth.py" file.
# Desc: Modules and libraries for login route.
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_security import login_user

# Desc: My own modules and libraries for login route.
from src.models.login import LoginForm
from src.utils.flask_security import user_datastore

# Desc: Blueprint for login route.
auth_blueprint = Blueprint('login', __name__)

# Desc: Login route.
@auth_blueprint.route('/')
def index():
    return redirect(url_for('login'))
                            
@auth_blueprint.route('/auth/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        render_template('login/login.html', form=form)
        email = form.email.data
        password = form.password.data
        user = user_datastore.get_user(email)
        if user and user_datastore.check_password_hash(user, password):
            login_user(user)
            return redirect(url_for('home.home'))
        else:
            flash('Email or password incorrect.', 'danger')
    return render_template('pages/login.html', form=form)