#Desc: Import the necessary modules and libraries for the login route
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse
from index import app, db
from src.forms.login_form import LoginForm
from src.forms.register_form import RegisterForm
from src.models.user import User
from src.forms.item_form import ItemForm
from src.models.item import Item


#Desc: Create the login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Username or Password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html', form = form)

#Desc: Create the logout route
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

#Desc: Create the register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form  = RegisterForm()
    if form.validate_on_submit():
        user = User(username = form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered!')
        return redirect(url_for('login'))
    return render_template('register.html', form = form)

@app.route('/item/new', methods=['GET', 'POST'])
def new_item():
    form = ItemForm()
    if form.validate_on_submit():
        item = Item(name=form.name.data, description=form.description.data)
        db.session.add(item)
        db.session.commit()
        flash('Your item has been created.')
        return redirect(url_for('index'))
    return render_template('new_item.html', title='New Item', form=form)

@app.route('/item/<id>', methods=['GET', 'POST'])
def edit_item(id):
    item = Item.query.get(id)
    form = ItemForm(obj=item)
    if form.validate_on_submit():
        form.populate_obj(item)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('index'))
    return render_template('edit_item.html', title='Edit Item', form=form)

@app.route('/item/<id>/delete', methods=['POST'])
def delete_item(id):
    item = Item.query.get(id)
    db.session.delete(item)
    db.session.commit()
    flash('Your item has been deleted.')
    return redirect(url_for('index'))