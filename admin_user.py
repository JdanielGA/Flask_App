# Desc: Modules and libraries to create de admin test user.
from flask import Flask
# Desc: My own modules and libraries to create de admin test user.
from config.config import db, Config
from src.models.user import User, Role, RolesUsers

#Create the Flask app.
def setup_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Config.init_app(app)
    # Desc: Create database if not exists.
    with app.app_context():
        db.create_all()
    return app

# Desc: Create the admin test user.
def create_admin_user(app, db):
    with app.app_context():
        # Desc: Check if the admin user exists.
        admin_user = User.query.filter(User.username == 'admin').first()
        if not admin_user:
            # Desc: Create the admin role if not exists.
            admin_role = Role.query.filter(Role.name == 'admin').first()
            if not admin_role:
                admin_role = Role(name='admin', description='Admin role with all permissions')
                db.session.add(admin_role)
                db.session.commit()

            # Desc: Create the admin user.
            admin_user = User(
                id=1001,
                username='admin',
                email='admin@localhost.com',
                fs_uniquifier='admin',)
            admin_user.password = 'admin'
            db.session.add(admin_user)
            db.session.commit()

            # Desc: Assign admin role to admin user.
            admin_role_user = RolesUsers(
                id=1001,
                user_id=admin_user.id,
                role_id=admin_role.id)
            db.session.add(admin_role_user)
            db.session.commit()


# Desc: Call the functions to create the admin test user.
app = setup_app()
create_admin_user(app, db)
print('Admin user created successfully.')
