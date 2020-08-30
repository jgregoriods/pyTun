from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, validators


class MayaForm(FlaskForm):
    baktun = IntegerField('baktun', [validators.NumberRange(min=0, max=19)])
    katun = IntegerField('katun')
    tun = IntegerField('tun')
    uinal = IntegerField('uinal')
    kin = IntegerField('kin')

    submit_maya = SubmitField('Convert')

    greg_day = IntegerField('greg_day')
    greg_month = IntegerField('greg_month')
    greg_year = IntegerField('greg_year')

    submit_greg = SubmitField('Convert')