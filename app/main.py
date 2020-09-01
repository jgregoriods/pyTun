from flask import Flask

from .views.convert import convert_blueprint


app = Flask(__name__)

app.register_blueprint(convert_blueprint, url_prefix='')
