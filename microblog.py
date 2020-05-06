from app import app, db # from the package app (as whole), importing the variable class instance of Flask, called app. As defined in __init__.py
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}