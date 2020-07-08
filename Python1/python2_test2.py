#課題2
import calendar
import datetime

today = datetime.date.today()
year = today.year
month = today.month
day = today.day

#閏年判定関数
def leap_check(year):
     if calendar.isleap(year):
        return True
     else:
          return False

