from wtforms import Form, IntegerField


class MayaForm(Form):
    baktun = IntegerField('baktun')
    katun = IntegerField('katun')
    tun = IntegerField('tun')
    uinal = IntegerField('uinal')
    kin = IntegerField('kin')
