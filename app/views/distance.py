from flask import Blueprint, render_template, request

from datetime import datetime
from ..models.maya_date import MayaDate


distance_blueprint = Blueprint('distance', __name__)


@distance_blueprint.route('/distance', methods=['GET', 'POST'])
def distance_template():
    if request.method == 'GET':
        today = datetime.now()
        maya_date = MayaDate({'day': today.day,
                              'month': today.month,
                              'year': today.year},
                             format='gregorian')

    elif request.method == 'POST':
        maya_date = MayaDate(list(map(int, [request.form['baktun'],
                                            request.form['katun'],
                                            request.form['tun'],
                                            request.form['uinal'],
                                            request.form['kin']])))

        dist_number = [0] + list(map(int, [request.form['dn-katun'],
                                           request.form['dn-tun'],
                                           request.form['dn-uinal'],
                                           request.form['dn-kin']]))

        operator = request.form['operator']

        if operator == 'PDI':
            next_date = maya_date + dist_number
        elif operator == 'ADI':
            next_date = maya_date - dist_number

        return render_template('dn.html', maya_date=maya_date,
                               next_date=next_date, dn=dist_number,
                               operator=operator)

    return render_template('dn.html', maya_date=maya_date,
                           next_date=maya_date, dn=[0, 0, 0, 0, 0],
                           operator='PDI')
