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
        if request.method == 'POST':
            id = form.id.data
            username = form.username.data
            email = form.email.data
            password = form.password.data
            password_confirmation = form.password_confirmation.data
            active = True
            role = form.roles.data
            print(f'Role from form: -{role}-')
            response, status = create_user(id, username, email, password, password_confirmation, active, role)
            if status == 'success':
                print(f'Response: {response} - Status: {status}')
                flash(response, status)
                return render_template('pages/register.html', form=form)
            else:
                print(f'Response: {response} - Status: {status}')
                flash(response, status)
                return render_template('pages/register.html', form=form)
    except Exception as e:
        flash(e)
        return render_template('pages/register.html', form=form)
            
    return render_template('pages/register.html', form=form)