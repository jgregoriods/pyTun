from flask import Flask, render_template, request, make_response

from models.dates import MayaDate
from models.forms import MayaForm


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home_template():
    maya_form = MayaForm()
    maya_date = MayaDate()
    if request.method == 'POST':
        maya_date = MayaDate([maya_form.baktun.data,
                              maya_form.katun.data,
                              maya_form.tun.data,
                              maya_form.uinal.data,
                              maya_form.kin.data])
    return render_template('home.html', maya_form=maya_form, maya_date=maya_date)
"""
    if request.method == 'GET':
        maya_date = MayaDate()

        gregorian_year = maya_date.gregorian['year']
        era = 'CE'
        if maya_date.gregorian['year'] < 0:
            gregorian_year = abs(gregorian_year) + 1
            era = 'BCE'

        return render_template('home.html', maya_date=maya_date, gregorian_year=gregorian_year, era=era)
    else:
        if 'maya-form' in request.form:
            maya_date = MayaDate([int(request.form['baktun']),
                                int(request.form['katun']),
                                int(request.form['tun']),
                                int(request.form['uinal']),
                                int(request.form['kin'])])
        elif 'gregorian-form' in request.form:
            year = int(request.form['greg-year'])
            maya_date = MayaDate({})

        gregorian_year = maya_date.gregorian['year']
        era = 'CE'
        if maya_date.gregorian['year'] < 0:
            gregorian_year = abs(gregorian_year) + 1
            era = 'BCE'

        return render_template('home.html', maya_date=maya_date, gregorian_year=gregorian_year, era=era)
"""

if __name__ == '__main__':
    app.run(debug=True)