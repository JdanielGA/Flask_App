# Desc: Modules and libraries for home route
from flask import Blueprint, render_template

# Desc: Blueprint for clients route
clients_blueprint = Blueprint('clients', __name__)   

# Desc: Clients route
@clients_blueprint.route('/clients')
def clients():
    return render_template('pages/clients.html')