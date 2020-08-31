from flask import Flask, render_template, request, make_response, redirect

from datetime import datetime
from .models.dates import MayaDate
from .models.forms import MayaForm


MONTHS = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}


app = Flask(__name__)

app.config['SECRET_KEY'] = 'any secret string'


@app.route('/', methods=['POST', 'GET'])
def home_template():
    if request.method == 'GET':
        today = datetime.now()
        maya_date = MayaDate({'day': today.day,
                              'month': today.month,
                              'year': today.year},
                              format='gregorian')

    elif request.method == 'POST':
        if 'submit-maya' in request.form:
            maya_date = MayaDate(list(map(int, [request.form['baktun'],
                                                request.form['katun'],
                                                request.form['tun'],
                                                request.form['uinal'],
                                                request.form['kin']])),
                                 constant=int(request.form['constant']))

        elif 'submit-greg' in request.form:
            year = int(request.form['greg-era'] + request.form['greg-year'])
            maya_date = MayaDate({'day': int(request.form['greg-day']),
                                  'month': int(request.form['greg-month']),
                                  'year': year},
                                  format='gregorian',
                                  constant=int(request.form['constant']))

        elif 'submit-jul' in request.form:
            year = int(request.form['jul-era'] + request.form['jul-year'])
            maya_date = MayaDate({'day': int(request.form['jul-day']),
                                  'month': int(request.form['jul-month']),
                                  'year': year},
                                  format='julian',
                                  constant=int(request.form['constant']))

    return render_template('home.html', maya_date=maya_date, months=MONTHS)