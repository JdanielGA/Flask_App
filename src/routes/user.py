''' Register Route '''
## Path: "src/routes/register.py".
# Desc: Modules and libraries for register route.
from flask import Blueprint, render_template, flash, request
# Desc: My own modules and libraries for register route.
from src.services.user import create_user
from src.routes.auth import login_required
from src.models.register import RegisterForm

# Desc: Blueprint for register route
user_blueprint = Blueprint('user', __name__,)

# Desc: Register route
@user_blueprint.route('/user/register', methods=['GET', 'POST'])
@login_required
def register():
    form = RegisterForm(request.form)
    try:
        if request.method == 'POST' and form.validate():
            id = form.id.data
            username = form.username.data
            email = form.email.data
            password = form.password.data
            password_confirmation = form.confirm_password.data
            roles = form.roles.data
            new_user = create_user(id, username, email, password, password_confirmation, roles)
            if new_user:
                flash(new_user)
                return render_template('pages/register.html', form=form)
            else:
                flash(new_user)
                return render_template('pages/register.html', form=form)
    except Exception as e:
        flash(e)
        return render_template('pages/register.html', form=form)
            
    return render_template('pages/register.html', form=form)