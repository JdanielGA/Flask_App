''' Tasks route '''
## Desc: Route "src/routes/tasks.py".
# Desc: Modules and libraries for tasks route
from flask import Blueprint, render_template
# Desc: My own modules and libraries for tasks route.
from src.routes.auth import login_required

# Desc: Blueprint for tasks route
tasks_blueprint = Blueprint('tasks', __name__)

# Desc: Tasks route
@tasks_blueprint.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
    return render_template('pages/tasks.html')