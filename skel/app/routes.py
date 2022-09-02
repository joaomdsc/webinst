# app/routes.py: Home page route

from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Joao'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Skeleton App', user=user,
                           posts=posts)
