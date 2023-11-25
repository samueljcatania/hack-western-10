from flask import render_template
from flask_login import login_required
from app.main import main


@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')


@main.route('/protected')
@login_required
def protected():
    return "This is a protected area"