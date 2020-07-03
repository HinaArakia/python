#課題2
import calendar
import datetime

today = datetime.date.today()
year = today.year
month = today.month
day = today.day

#閏年判定関数
def leap_check(year,month,day):
     if calendar.isleap(year):
          print(str(year) + "年は閏年です")
     else:
          print(str(year) + "年は平年です")

leap_check(year, month, day)
leap_check(year - 1, month, day)
leap_check(year + 1, month, day)
