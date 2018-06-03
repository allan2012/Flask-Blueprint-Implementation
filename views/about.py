from flask import Blueprint, render_template
from flask import request
from wtforms import Form, BooleanField, StringField, PasswordField, validators

about = Blueprint('about', __name__, template_folder='templates')

class RegistrationForm(Form):
    name = StringField('name', [validators.Length(min=4, max=25)])

@about.route('/')
def list():
    return "Hello Allan"

@about.route('/post_name', methods=['POST'])
def post_name():
    f = RegistrationForm(request.form)
    if request.method == 'POST' and f.validate():
        return "You are looking to find: " + request.form['name']
    return render_template('home/index.html')