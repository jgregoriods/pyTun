from astropy.time import Time
from math import floor, ceil
from typing import List, Dict, Union, Tuple


class MayaDate:
    """
    A class used to represent a date in the Maya, Gregorian and Julian
    calendars.
    """

    TZOLKIN_NAMES = ['Ahau', 'Imix', 'Ik', 'Akbal', 'Kan', 'Chicchan', 'Cimi',
                     'Manik', 'Lamat', 'Muluc', 'Oc', 'Chuen', 'Eb', 'Ben',
                     'Ix', 'Men', 'Cib', 'Caban', 'Etznab', 'Cauac']

    HAAB_NAMES = ['Pop', 'Uo', 'Zip', 'Zotz', 'Tzec', 'Xul', 'Yaxkin', 'Mol',
                  'Chen', 'Yax', 'Zac', 'Ceh', 'Mac', 'Kankin', 'Muan', 'Pax',
                  'Kayab', 'Cumku', 'Uayeb']

    MONTHS = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
              'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

    def __init__(self, date: Union[List, Dict] = None,
                 format: str = 'long_count', constant: int = 584283):
        """
        When initializing with Maya calendar, date must be given as a
        list representing the Long Count. When initializing with one of
        the western calendars, date must be given as a dictionary
        specifying year (negative if BCE), month and day. Date is
        initialized as 0.0.0.0.0 4 Ahau 8 Cumku if empty.
        """

        self.constant = constant

        if format == 'long_count':
            self.long_count = date or [0, 0, 0, 0, 0]
            self.julian_day = (MayaDate.to_decimal(self.long_count)
                               + self.constant)
            self.gregorian = self.get_gregorian()
            self.julian = self.get_julian()

        elif format == 'gregorian':
            self.gregorian = date or {'year': -3113, 'month': 8, 'day': 11}
            self.julian_day = ceil(Time(self.gregorian).jd)
            self.long_count = self.get_long_count()
            self.julian = self.get_julian()

        elif format == 'julian':
            self.julian = date or {'year': -3113, 'month': 9, 'day': 6}
            self.julian_day = (ceil(Time(self.julian).jd) +
                               MayaDate.julian_offset(self.julian))
            self.gregorian = self.get_gregorian()
            self.long_count = self.get_long_count()

        self.tzolkin = self.get_tzolkin()
        self.haab = self.get_haab()
        self.lord_of_night = self.get_lord_of_night()

    def get_gregorian(self) -> Dict:
        """Converts the date to the Gregorian calendar."""

        jd = Time(self.julian_day, format='jd')
        jd.format = 'ymdhms'

        return {
            'year': jd.value.year,
            'month': jd.value.month,
            'day': jd.value.day
            }

    def get_long_count(self) -> List:
        """Converts the date to the Maya Long Count."""

        long_count = MayaDate.to_vigesimal(self.julian_day - self.constant)

        return long_count

    def get_julian(self) -> Dict:
        """Converts the date to the Julian calendar."""

        jd = Time(self.julian_day - MayaDate.julian_offset(self.gregorian),
                  format='jd')
        jd.format = 'ymdhms'

        return {
            'year': jd.value.year,
            'month': jd.value.month,
            'day': jd.value.day
            }

    def get_tzolkin(self) -> Tuple:
        """
        Calculates the date in the Maya Tzolkin (260-day) calendar from
        the Long Count.
        """

        n_days = MayaDate.to_decimal(self.long_count)
        # Adjust for the offset of 4 Ahau
        coef = (n_days + 3) % 13 + 1
        name = MayaDate.TZOLKIN_NAMES[n_days % 20]

        return (coef, name)

    def get_haab(self) -> Tuple:
        """
        Calculates the date in the Maya Haab (365-day) calendar from
        the Long Count.
        """

        n_days = MayaDate.to_decimal(self.long_count)
        # Adjust for the offset of 8 Cumku
        year_day = (n_days + 348) % 365

        if year_day > 360:
            coef = year_day - 360
            name = 'Uayeb'

        else:
            coef = year_day % 20
            name = MayaDate.HAAB_NAMES[floor(year_day / 20)]

        return (coef, name)

    def get_lord_of_night(self) -> str:
        """
        Calculates the day in the G series (9-day cycle) of the Maya
        calendar from the Long Count.
        """

        index = MayaDate.to_decimal(self.long_count) % 9

        if index == 0:
            return 'G9'

        else:
            return f'G{index}'

    def __str__(self) -> str:
        long_count = '.'.join(map(str, self.long_count))
        tzolkin = ' '.join(map(str, self.tzolkin))
        haab = ' '.join(map(str, self.haab))

        return f'{long_count} {tzolkin} {haab}'

    def __add__(self, distance_number):
        if isinstance(distance_number, list):
            n_days = (MayaDate.to_decimal(self.long_count)
                      + MayaDate.to_decimal(distance_number))
            return MayaDate(MayaDate.to_vigesimal(n_days),
                            constant=self.constant)

    def __sub__(self, distance_number):
        if isinstance(distance_number, list):
            n_days = (MayaDate.to_decimal(self.long_count)
                      - MayaDate.to_decimal(distance_number))
            return MayaDate(MayaDate.to_vigesimal(n_days),
                            constant=self.constant)

    @staticmethod
    def to_vigesimal(decimal: int) -> List:
        """Converts a decimal number to the Maya vigesimal system."""

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
    def to_decimal(vigesimal: List) -> int:
        """Converts a Maya vigesimal number to the decimal system."""

        vigesimal_places = [144000, 7200, 360, 20, 1]
        decimal = sum(x * y for x, y in zip(vigesimal, vigesimal_places))

        return decimal

    @staticmethod
    def julian_offset(date: Dict) -> int:
        """
        Calculates the difference in days between the Gregorian and
        Julian calendars.
        """

        # Last alignment between Gregorian and Julian Calendars was
        # Feb 1 200 CE
        n_days = Time(date).jd - Time({'year': 200, 'month': 2, 'day': 1}).jd
        centuries = n_days // 36524
        extra_leap = (centuries + 2) // 4

        return int(centuries - extra_leap)
