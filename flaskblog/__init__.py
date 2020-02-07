from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '3eb1cfb7d8138819aabbaedf1c9198bc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LfzJtMUAAAAAA_3iwzND9XUTgzgs0GiGHsqignG'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LfzJtMUAAAAAAf6Ce_1BTcTbX0RNhIvaipmvev0' 
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from flaskblog import routes