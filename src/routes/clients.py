# Desc: Modules and libraries for home route
from flask import Blueprint, render_template, request, redirect, url_for, flash
# Desc: My own modules and libraries for home route
from config.config import db
from src.routes.auth import login_required
from src.models.clients import Client, ClientForm
from src.services.clients import ClientServices

# Desc: Blueprint for clients route
clients_blueprint = Blueprint('clients', __name__)   

# Desc: Clients route
@clients_blueprint.route('/clients')
@login_required
def clients():
    clients = Client.query.all()
    return render_template('pages/clients.html', clients=clients)

# Desc: Create client route
@clients_blueprint.route('/clients/create')
@login_required
def create_client():
    return render_template('pages/create_client.html')