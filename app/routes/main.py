from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def landing_page():
    return render_template('landing.html')
