from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY']='1657586a8b4ce0bb31ad2f5caf052a72'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///omar.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

bcrypt = Bcrypt()

from omar import routes
