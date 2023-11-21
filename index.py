# Desc: Modules and libraries for launch the app.
from flask import Flask, g
# Desc: My own modules and libraries for launch the app.
from config.config import Config, db
from src.routes.home import home_blueprint
from src.routes.clients import clients_blueprint
from src.routes.auth import auth_blueprint
from src.routes.calendar import calendar_blueprint
from src.routes.tasks import tasks_blueprint
from src.routes.user import user_blueprint

# Desc: Create and config the app.
app = Flask(__name__, template_folder='src/templates', static_folder='src/static')
app.config.from_object(Config)
db.init_app(app)

# Desc: Blueprint of the app.
app.register_blueprint(auth_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(clients_blueprint)
app.register_blueprint(tasks_blueprint)
app.register_blueprint(calendar_blueprint)
app.register_blueprint(user_blueprint)

@app.context_processor
def inject_user():
    return dict(user=g.user)

# Desc: Launch the app.
if __name__ == '__main__':
    app.run(debug=True, port=5000)