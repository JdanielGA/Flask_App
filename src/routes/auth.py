''' Aunthentication route '''
## Path: "src/routes/auth.py".
# Desc: Modules and libraries for login route.
from flask import Blueprint, render_template, request, redirect, url_for, flash, session, g
import functools

# Desc: My own modules and libraries for login route.
from src.models.login import LoginForm
from src.services.user import login_user
from src.models.user import User

# Desc: Blueprint for login route.
auth_blueprint = Blueprint('login', __name__)

# Desc: Login route.
@auth_blueprint.route('/')
@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        user = login_user(username, password)
        if user:
            session.clear()
            session['username'] = username
            return redirect(url_for('home.home'))
        else:
            flash('username or password incorrect')
            return redirect(url_for('login.login'))
    return render_template('pages/login.html', form=form)

# Desc: g object to get the user.
@auth_blueprint.before_app_request
def load_logged_in_user():
    username = session.get('username')
    if username is None:
        g.user = None
    else:
        g.user = User.query.filter_by(username=username).first()

# Desc: Decorator to force the user to login.
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('login.login'))
        return view(**kwargs)
    return wrapped_view

# Desc: Logout route.
@auth_blueprint.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login.login'))