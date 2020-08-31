import datetime

from astropy.time import Time
from math import floor, ceil


tzolkin_names = ['Ahau', 'Imix', 'Ik', 'Akbal', 'Kan', 'Chicchan', 'Cimi',
                 'Manik', 'Lamat', 'Muluc', 'Oc', 'Chuen', 'Eb', 'Ben', 'Ix',
                 'Men', 'Cib', 'Caban', 'Etznab', 'Cauac']

haab_names = ['Pop', 'Uo', 'Zip', 'Zotz', 'Tzec', 'Xul', 'Yaxkin', 'Mol',
              'Chen', 'Yax', 'Zac', 'Ceh', 'Mac', 'Kankin', 'Muan', 'Pax',
              'Kayab', 'Cumku', 'Uayeb']


class MayaDate:
    def __init__(self, date=[0, 0, 0, 0, 0], format='long_count', constant=584283):
        self.constant = constant

        if format == 'long_count':
            self.long_count = date
            self.julian_day = MayaDate.to_decimal(date) + constant
            self.gregorian = self.get_gregorian()
            self.julian = self.get_julian()
        
        elif format == 'gregorian':
            self.gregorian = date
            self.julian_day = ceil(Time(date).jd)
            self.long_count = self.get_long_count()
            self.julian = self.get_julian()

        elif format == 'julian':
            self.julian = date
            self.julian_day = ceil(Time(date).jd) + MayaDate.julian_offset(date)
            self.gregorian = self.get_gregorian()
            self.long_count = self.get_long_count()

        self.tzolkin = self.get_tzolkin()
        self.haab = self.get_haab()

    def get_gregorian(self):
        jd = Time(self.julian_day, format='jd')
        jd.format = 'ymdhms'

        return {
            'year': jd.value.year,
            'month': jd.value.month,
            'day': jd.value.day
            }

    def get_long_count(self):
        return MayaDate.to_vigesimal(self.julian_day - self.constant)

    def get_julian(self):
        jd = Time(self.julian_day - MayaDate.julian_offset(self.gregorian), format='jd')
        jd.format = 'ymdhms'

        return {
            'year': jd.value.year,
            'month': jd.value.month,
            'day': jd.value.day
            }

    def get_tzolkin(self):
        n_days = MayaDate.to_decimal(self.long_count)
        # Adjust for the offset of 4 Ahau
        coef = (n_days + 3) % 13 + 1
        name = tzolkin_names[n_days % 20]
        return [coef, name]

    def get_haab(self):
        n_days = MayaDate.to_decimal(self.long_count)
        # Adjust for the offset of 8 Cumku
        year_day = (n_days + 348) % 365
        if year_day > 360:
            coef = year_day - 360
            name = 'Uayeb'
        else:
            coef = year_day % 20
            name = haab_names[floor(year_day / 20)]
        return [coef, name]

    def __str__(self):
        long_count = '.'.join(map(str, self.long_count))
        tzolkin = ' '.join(map(str, self.tzolkin))
        haab = ' '.join(map(str, self.haab))

        return f'{long_count} {tzolkin} {haab}'

    @staticmethod
    def to_vigesimal(decimal):
        vigesimal = [0, 0, 0, 0, 0]

        vigesimal[0] = decimal // 144000
        decimal %= 144000

        vigesimal[1] = decimal // 7200
        decimal %= 7200

        vigesimal[2] = decimal // 360
        decimal %= 360

        vigesimal[3] = decimal // 20
        decimal %= 20

        vigesimal[4] = decimal

        return vigesimal

    @staticmethod
    def to_decimal(vigesimal):
        multiples = [144000, 7200, 360, 20, 1]
        decimal = sum(x * y for x, y in zip(vigesimal, multiples))
        return decimal

    @staticmethod
    def julian_offset(date):
        #return ceil(year / 100) - 3 - (year // 400)
        # Last alignment between Gregorian and Julian Calendars was Feb 1 200
        n_days = Time(date).jd - Time({'year': 200, 'month': 2, 'day': 1}).jd
        centuries = n_days // 36524
        extra_leap = (centuries + 2) // 4
        return int(centuries - extra_leap)