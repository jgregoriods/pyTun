from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, validators


class MayaForm(FlaskForm):
    baktun = IntegerField('baktun', [validators.NumberRange(min=0, max=19)])
    katun = IntegerField('katun')
    tun = IntegerField('tun')
    uinal = IntegerField('uinal')
    kin = IntegerField('kin')