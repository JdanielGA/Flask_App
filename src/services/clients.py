''' Client services. '''
## Path: "src/services/clients.py".
# Desc: My own modules and libraries for client services.
from config.config import db
from src.models.clients import Client

# Desc: Funtion to create a new client.
class ClientServices:
    def __init__(self, db, nit, name, lastname, email, phone, address, city, state, notes):
        self.db = db
        self.nit = nit
        self.name = name
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state
        self.notes = notes

    def create_client(self):
        # Desc: Check if the NIT or already exists.
        client = Client.query.filter_by(nit=self.nit).first()
        if client:
            return ('NIT already exists in the database!', 'error')
        # Desc: Check if the email already exists.
        client = Client.query.filter_by(email=self.email).first()
        if client:
            return ('Email already exists in the database!', 'error')
        
        # Desc: Create the client.
        client = Client(
            nit=self.nit,
            name=self.name,
            lastname=self.lastname,
            email=self.email,
            phone=self.phone,
            address=self.address,
            city=self.city,
            state=self.state,
            notes=self.notes)
        db.session.add(client)
        db.session.commit()

        return ('Client created successfully!', 'success')
    
    # Desc: Funtion to get all clients.
    def get_clients(self):
        clients = Client.query.all()
        if not clients:
            return None
        return clients
    
    # Desc: Funtion to get a client by id.
    def get_client_by_id(self):
        client = Client.query.filter_by(id=self.id).first()
        if not client:
            return ('The client does not exist!', 'error')
        message = 'success'
        return client, message
    
    # Desc: Funtion to get a client by nit.
    def get_client_by_nit(self):
        client = Client.query.filter_by(nit=self.nit).first()
        if not client:
            return ('The client does not exist!', 'error')
        return client
    
    # Desc: Funtion to get a client by name.
    def get_client_by_name(self):
        client = Client.query.filter_by(name=self.name).first()
        if not client:
            return ('The client does not exist!', 'error')
        return client
    
    # Desc: Funtion to get a client by lastname.
    def get_client_by_lastname(self):
        client = Client.query.filter_by(lastname=self.lastname).first()
        if not client:
            return ('The client does not exist!', 'error')
        return client
    
    # Desc: Funtion to get a client by email.
    def get_client_by_email(self):
        client = Client.query.filter_by(email=self.email).first()
        if not client:
            return ('The client does not exist!', 'error')
        return client
    
    # Desc: Funtion to get a client by phone.
    def get_client_by_phone(self):
        client = Client.query.filter_by(phone=self.phone).first()
        if not client:
            return ('The client does not exist!', 'error')
        return client
    
    # Desc: Funtion to update a client by id.
    def update_client_by_id(self):
        client = Client.query.filter_by(id=self.id).first()
        if not client:
            return ('The client does not exist!', 'error')
        client.name = self.name
        client.lastname = self.lastname
        client.email = self.email
        client.phone = self.phone
        client.address = self.address
        client.city = self.city
        client.state = self.state
        client.notes = self.notes
        db.session.commit()
        return ('Client updated successfully!', 'success')
    
    # Desc: Funtion to update a client by nit.
    def update_client_by_nit(self):
        client = Client.query.filter_by(nit=self.nit).first()
        if not client:
            return ('The client does not exist!', 'error')
        client.name = self.name
        client.lastname = self.lastname
        client.email = self.email
        client.phone = self.phone
        client.address = self.address
        client.city = self.city
        client.state = self.state
        client.notes = self.notes
        db.session.commit()
        return ('Client updated successfully!', 'success')
    
    # Desc: Funtion to delete a client by id.
    def delete_client_by_id(self):
        client = Client.query.filter_by(id=self.id).first()
        if not client:
            return ('The client does not exist!', 'error')
        db.session.delete(client)
        db.session.commit()
        return ('Client deleted successfully!', 'success')
    
    # Desc: Funtion to delete a client by nit.
    def delete_client_by_nit(self):
        client = Client.query.filter_by(nit=self.nit).first()
        if not client:
            return ('The client does not exist!', 'error')
        db.session.delete(client)
        db.session.commit()
        return ('Client deleted successfully!', 'success')