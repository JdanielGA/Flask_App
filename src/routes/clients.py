# Desc: Modules and libraries for home route
from flask import Blueprint, jsonify, render_template, request, redirect, url_for, flash
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

# Desc: Create client route using de service.
@clients_blueprint.route('/clients/create', methods=['GET', 'POST'])
@login_required
def create_client():
    form = ClientForm(request.form)
    try:
        if request.method == 'POST':            
            nit = form.nit.data
            name = form.name.data
            lastname = form.lastname.data
            email = form.email.data
            phone = form.phone.data
            address = form.address.data
            city = form.city.data
            state = form.state.data
            notes = form.notes.data
            response, status = ClientServices(
                db=db,
                nit=nit,
                name=name,
                lastname=lastname,
                email=email,
                phone=phone,
                address=address,
                city=city,
                state=state,
                notes=notes).create_client()
            if status == 'success':
                print(f'Response: {response} - Status: {status}')
                flash(response, status)
                return redirect(url_for('clients.clients'))
            else:
                print(f'Response: {response} - Status: {status}')
                flash(response, status)
                return render_template('pages/create_client.html', form=form)
    except Exception as e:
        flash(e)
        return render_template('pages/create_client.html')
    
    return render_template('pages/create_client.html', form=form)

# Desc: Search client route
@clients_blueprint.route('/clients/search', methods=['GET'])
@login_required
def search_client():
    query = request.args.get('query')
    clients = Client.query.filter(Client.name.ilike(f"%{query}%")).all()
    return jsonify([client.serialize() for client in clients])

# Desc: Update client route using de service.
@clients_blueprint.route('/clients/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_client(id):
    pass

# Desc: Delete client route.
@clients_blueprint.route('/clients/delete/<int:id>')
@login_required
def delete_client(id):
    client = Client.query.filter_by(id=id).first()
    db.session.delete(client)
    db.session.commit()
    flash('Client deleted successfully!', 'success')
    return redirect(url_for('clients.clients'))