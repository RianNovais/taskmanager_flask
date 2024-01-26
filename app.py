from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#In this file we will have our app's settings, and everything related to it.

app = Flask(__name__)
app.config.from_object('config')

#config db

db = SQLAlchemy(app)

#config migrate object to perform migrations

migrate = Migrate(app, db)

#importing the routes that will make up the app
from controllers import routes
#importing the model tables for migration
from models import tables