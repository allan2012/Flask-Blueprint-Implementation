from flask import Blueprint, render_template

home = Blueprint('home', __name__, template_folder='templates')

@home.route('/')
def list():
    name = "James Alotei"
    return render_template('home/index.html', name=name)


@home.route('/create')
def create():
    return "Hello Create"


@home.route('/happy')
def happy():
    return "This is a happy day"