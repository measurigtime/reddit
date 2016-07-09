from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Rahil'}
    posts = [  # fake array of posts
            {
                'author': {'nickname': 'John'},
                'body': "A beautiful day in Portland!"
            },
            {
                'author': {'nickname': 'Susan'},
                'body': 'The Avengers movie was so cool!'
            }
        ]
    return render_template('index.html', title='Home', user=user, posts=posts)
