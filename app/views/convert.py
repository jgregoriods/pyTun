from flask import Flask, Blueprint, render_template, request, make_response, \
                  redirect

from datetime import datetime
from ..models.maya_date import MayaDate
from ..utils import MONTHS


convert_blueprint = Blueprint('convert', __name__)


@convert_blueprint.route('/', methods=['GET', 'POST'])
def convert_template():
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
