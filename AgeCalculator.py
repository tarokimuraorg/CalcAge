from datetime import date
from datetime import timedelta
from datetime import timezone
from datetime import datetime
import math
from ErrorMessageCreator import ErrorMessageCreator

class AgeCalculator:
    
    def __init__(self):

        self._emcreator = ErrorMessageCreator()

        time_diff = timedelta(hours=9)
        jst = timezone(time_diff,'JST')
        
        self._today = datetime.now(jst).date()

    def age(self, year: int, month: int, day: int) -> int:

        age = -1

        try:

            date_of_birth = date(year,month,day)
            delta = self._today - date_of_birth
            age = int(delta.days) / 365

        except ValueError as ve:

            raise ValueError(self._emcreator.message('AgeCalculator', 'age', 'invalid argument', '{}.'.format(ve)))

        if age > 0 or age == 0:
            return math.floor(age)

        raise ValueError(self._emcreator.message('AgeCalculator', 'age', 'invalid argument', 'the argument is out of range for date of birth.'))
