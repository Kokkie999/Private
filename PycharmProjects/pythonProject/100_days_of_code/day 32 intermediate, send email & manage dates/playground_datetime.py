import datetime as dt

now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()
print(day_of_week)


date_of_birth = dt.datetime(year=1968 , month=12 , day=7)
print(date_of_birth)
