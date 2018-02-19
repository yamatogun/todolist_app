from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os.path as osp

from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

# db in the same dir than the init file of app package
dirpath = osp.dirname(osp.abspath(__file__))
dbname = 'data.db'
dbpath = osp.join(dirpath, dbname)
print dbpath

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + dbpath
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False  # True
db = SQLAlchemy(app)


# login system
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'  # corresponding view file in templates/

# CRSF protection
csrf = CSRFProtect(app) 
app.config['SECRET_KEY'] = 'secretkey'

# need Models class to create corresponding tables in db
from models import User # after creation of db and login manager

from . import views
