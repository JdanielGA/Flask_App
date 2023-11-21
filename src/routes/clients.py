# Desc: Modules and libraries for home route
from flask import Blueprint, render_template
# Desc: My own modules and libraries for home route
from src.routes.auth import login_required

# Desc: Blueprint for clients route
clients_blueprint = Blueprint('clients', __name__)   

# Desc: Clients route
@clients_blueprint.route('/clients')
@login_required
def clients():
    return render_template('pages/clients.html')