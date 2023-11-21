''' Calendar Route '''
## Desc: Route "src/routes/calendar.py".
# Desc: Modules and libraries for calendar route.
from flask import Blueprint, render_template
# Desc: My own modules and libraries for calendar route.
from src.routes.auth import login_required

# Desc: Blueprint for calendar route
calendar_blueprint = Blueprint('calendar', __name__)

# Desc: Calendar route
@calendar_blueprint.route('/calendar', methods=['GET', 'POST'])
@login_required
def calendar():
    return render_template('pages/calendar.html')