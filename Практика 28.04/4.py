
import datetime
day='4'
mount='12'
year='2001'
days=100000
datea=datetime.date(int(year), int(mount), int(day))
print(datea)
dateb=datetime.timedelta(days=days)
print(dateb)
print(datea+dateb)