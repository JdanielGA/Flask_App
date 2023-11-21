''' Home route '''
## Desc: Route "src/routes/home.py".
# Desc: Modules and libraries for home route
from flask import Blueprint, render_template
from src.routes.auth import login_required

# Desc: Blueprint for home route
home_blueprint = Blueprint('home', __name__)   

# Desc: Home route
@home_blueprint.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('pages/home.html')