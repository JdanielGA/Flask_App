# Desc: Modules and libraries for launch the app.
from flask import Flask

# Desc: My own modules and libraries for launch the app.
from config.config import Config
from src.routes.home import home_blueprint
from src.routes.clients import clients_blueprint


# Desc: Create and config the app.
app = Flask(__name__, template_folder='src/templates')
app.config.from_object(Config)

# Desc: Blueprint of the app.
app.register_blueprint(home_blueprint)
app.register_blueprint(clients_blueprint)

# Desc: Launch the app.
if __name__ == '__main__':
    app.run(debug=True, port=5000)