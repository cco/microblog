from flask import Flask
from config import Config

app = Flask(__name__) # var app created as an instance of Flask. This makes var app a member of app package (directory is package).
app.config.from_object(Config) # Tells Flask to read and apply configuration from Config class within config.py

from app import routes # ref to app here is referring to directory app. Importing routes.py