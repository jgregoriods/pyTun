from flask import Flask

from .views.convert import convert_blueprint


app = Flask(__name__)

app.config['SECRET_KEY'] = 'any secret string'

app.register_blueprint(convert_blueprint, url_prefix='')
