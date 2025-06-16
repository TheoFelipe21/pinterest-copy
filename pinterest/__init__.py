from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pinterest.db'
app.config["SECRET_KEY"] = "e4e6b6934fad33a7727800f2d306cb27"
app.config['UPLOAD_FOLDER'] = "static/fotos_post"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'home'

from pinterest import routes