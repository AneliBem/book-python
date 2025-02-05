from datetime import date
now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

birhday = date(2004, 12, 5)
age = now - birhday
print(age.days)