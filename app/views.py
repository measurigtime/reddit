from flask import render_template, flash, redirect, url_for, g
from app import app, db, lm
from models import User
from oauth import OAuthSignIn
from .forms import LoginForm
from flask_login import login_user, logout_user, current_user, login_required


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
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


@app.route('/login', methods=['GET'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()

    return render_template(
        'login.html', title='Sign In',
        form=form
    )


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email = oauth.callback()
    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('index'))
    user = User.query.filter_by(social_id=social_id).first()
    if not user:
        user = User(social_id=social_id, nickname=username, email=email)
        db.session.add(user)
        db.session.commit()
    login_user(user, True)
    return redirect(url_for('index'))
