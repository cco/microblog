from flask import render_template
from app import app

@app.route('/') # @ denotes decorators. Modifies function that follows
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Chris'},
            'body': 'Oi mate, today was aight!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)