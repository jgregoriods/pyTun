from flask import Flask, render_template, request, make_response, redirect

from models.dates import MayaDate
from models.forms import MayaForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'any secret string'


@app.route('/')
def home_template():
    maya_date = MayaDate()
  
    maya_form = MayaForm(obj=maya_date, baktun=maya_date.long_count[0],
                                        katun=maya_date.long_count[1],
                                        tun=maya_date.long_count[2],
                                        uinal=maya_date.long_count[3],
                                        kin=maya_date.long_count[4],
                                        
                                        greg_day=maya_date.gregorian['day'],
                                        greg_month=maya_date.gregorian['month'],
                                        greg_year=maya_date.gregorian['year'])

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

@app.route('/convert', methods=['POST'])
def convert_template():

    if 'submit_maya' in request.form:
        maya_date = MayaDate([int(request.form['baktun']),
                              int(request.form['katun']),
                              int(request.form['tun']),
                              int(request.form['uinal']),
                              int(request.form['kin'])])

        new_maya_form = MayaForm()
        new_maya_form.greg_year.value = maya_date.gregorian['year']

    return render_template('home.html', maya_form=new_maya_form, maya_date=maya_date)

if __name__ == '__main__':
    app.run(debug=True)