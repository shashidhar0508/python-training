import datetime as dt
from datetime import timedelta

print("Get Current Date and Time : ",dt.datetime.now())

print("Get Current Date : ",dt.date.today())

# Formatting Date and Time Output with Strftime()
now=dt.datetime.now()
print("print full year with century using Strftime() : ",now.strftime("%Y"))
print("print full year without century using Strftime() : ",now.strftime("%y"))
print(" Strf function can declare the date, day, month and year separately : ",now.strftime("%a,%d,%B,%y"))
print(" Strf function to declare local date and time, local date, local time : ",now.strftime("%c,%x,%X"))

# Timedelta in Python
print("One year from now using timedelta() : ",str(dt.datetime.now()+timedelta(days=365)))
print("future date from now using timedelta() : ",str(dt.datetime.now()+timedelta(weeks=1,days=5)))