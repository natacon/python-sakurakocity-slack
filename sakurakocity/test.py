import datetime

print(datetime.date.today())
print(datetime.date(2016, 3, 7))

couple_date = datetime.date(2015, 3, 7)
marrige_date = datetime.date(2016, 3, 7)
now = datetime.date.today()
print((now-marrige_date).days)
