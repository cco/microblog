from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__) # var app created as an instance of Flask. This makes var app a member of app package (directory is package).
app.config.from_object(Config) # Tells Flask to read and apply configuration from Config class within config.py
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models # ref to app here is referring to directory app. Importing routes.py