# Code mostly sourced by https://github.com/miguelgrinberg/microblog with some deletions and additions for our use case.

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask import Blueprint

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
bootstrap = Bootstrap(app)
bp = Blueprint('api', __name__)

from app import routes, models
from app.api import addresses
app.register_blueprint(bp, url_prefix='/api')
