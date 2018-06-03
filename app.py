from flask import Flask
from views.home import home
from views.about import about


app = Flask(__name__)
app.register_blueprint(home, url_prefix='/')
app.register_blueprint(about, url_prefix='/about')

app.config['DEBUG'] = True

if __name__ == '__main__':
    app.logger.debug('A value for debugging')
    app.run('0.0.0.0')