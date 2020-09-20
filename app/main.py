from flask import Flask

from .views.convert import convert_blueprint
from .views.distance import distance_blueprint


app = Flask(__name__)

app.register_blueprint(convert_blueprint, url_prefix='')
app.register_blueprint(distance_blueprint, url_prefix='')