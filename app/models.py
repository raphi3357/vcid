# Managing the database, objects that should be written into the database. Code partly sourced by https://github.com/miguelgrinberg/microblog

from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# Standard user class, representing a registered user with name, email and password
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    addresses = db.relationship('Address', backref='author', lazy='dynamic')
    email = db.Column(db.String(120), index=True, unique=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

# Monitoring object which a user can create and watch.
class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    lastStatus = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Address {}>'.format(self.body)

    # function used by to get data out to the api in JSON format
    def to_dict(self):
        return {
            'id': self.id,
            'body': self.body
        }

@login.user_loader
def load_user(id):
    return User.query.get(int(id))