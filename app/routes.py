from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Address
from werkzeug.urls import url_parse
import sys, requests
from app.forms import AddressForm

# Route for the main page with the addresses and possibility to add new monitoring objects
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    # Form to add new address (monitoring url)
    form = AddressForm()
    if form.validate_on_submit():
        address = Address(body=form.address.data, author=current_user)
        db.session.add(address)
        db.session.commit()
        flash('Monitoring object added!')
        return redirect(url_for('index'))

    # Querying all the addresses for the current user
    addresses = Address.query.filter_by(user_id=User.query.filter_by(username=current_user.username).first().id).all()

    # Getting the status for the queried users
    for a in addresses:
        try:
            if requests.get(a.body, timeout=1).ok:
                a.lastStatus = True
        except Exception as e:
            print(e, sys.stderr)

    return render_template("index.html", title='Home Page', form=form, addresses=addresses)

# Standard login/-out, register and edit profile page and form, sourced by https://github.com/miguelgrinberg/microblog

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.username.data = current_user.username
    return render_template('edit_profile.html', title='Edit Profile', form=form)

# Route to delete an address by providing an id
@app.route('/delete/<int:id>')
def delete(id):
    db.session.delete(Address.query.get_or_404(id))
    db.session.commit()
    flash("Object deleted successfully.")
    return redirect(url_for('index'))

