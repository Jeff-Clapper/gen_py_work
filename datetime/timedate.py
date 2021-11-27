# Currently on 8:26 of #30: Working with Python date & time (datetime module) | Python for Beginners

"""Practice session with Dates"""
# """This method of converting numbers into a datetime.date class will work"""
# import datetime as dt
# date1 = dt.date(2020,6,13)
# print(date1)
# print(type(date1))

"""This method of converting numbers into a datetime.date class will work"""
from datetime import date 

# accepts number in year, month, day format and converts to a date object
date1 = date(2020,6,13)
# print(f'{date1}\n')
# print(f'{type(date1)}\n')

today = date.today()
# print(f'{today}\n')

# the datetime.date class can add a .year or .month or .day to get the value of just that portion of the date 
# print(f'{today.year}')
# print(f'{today.month}')
# print(f'{today.day}\n')

# """this method will not work as the date function falls under the date class rather than the datetime class. datetime is what we import from and what we are importing.
# In this case, we are trying to call the import datetime, but should really be calling date"""
# from datetime import datetime
# date1 = datetime.date(2020,6,13)
# print(date1)
"""Datetime's TIME work"""
"""May need to look into Time module as it may be more effective at working with time?"""
from datetime import time

# accepts number in hour, minute, second, microsecond format and converts to a time object
time1 = time(12,22,30)
# print(time1,"\n")
time1 = time(13,22,30,653876)
# print(time1,"\n")

# print(f'hour: {time1.hour}')
# print(f'minute: {time1.minute}')
# print(f'second: {time1.second}')
# print(f'microsecond: {time1.microsecond}')


from datetime import datetime
"""DATETIME work"""

# accepts number in year, month, day, hour, minute, second, microsecond format and converts to a datetime object
datetime_obj = datetime(2021, 11, 20, 15, 35, 58, 44004)
# print(datetime_obj, "\n")
# print(f'date: {datetime_obj.date()}')
# print(f'time: {datetime_obj.time()}\n')

# getting current date and time
current_date_time = datetime.now()
# print(current_date_time.date())
# print(current_date_time.time(), "\n")

# datetime.replace will change out a portion of the date and time to a new value
next_saturday = current_date_time.replace(day = current_date_time.day + 7)
# print(f'next saturday: {next_saturday}\n')


"""Working on timedelta below"""
from datetime import timedelta

today = datetime.now()
next_new_year = datetime(2022,1,1,0,0,0,1)

time_remaining_to_year = next_new_year-today
# print(time_remaining_to_year)


"""Working with strftime()"""
# print(today)

string_date = today.strftime("%A %B %m, %Y")
day_of_week = today.strftime("%A")
string_time = today.strftime("%I:%M %p")

print(string_date)
print(string_time)
print(f"Day of the week: {day_of_week}\n")




datetime_date = datetime.strptime(string_date,"%A %B %m, %Y")
print(datetime_date)
"""TIME ZONE WORK IS TRICKY, RECOMMENDED TO USE THE pytz 2021.1 module, install with pip install pytz"""

# I was just messing around on my own below
# print("\n")
date1 = date.fromisoformat("2011-11-04")
date2 = date(2020,6, 13)
# print(date2)

# print(f"date 1: {date1}")
# print(f"date 2: {date2}\n")

# print(f"this is today's date: {today}")
lw = today.replace(day = today.day-7)
# print(f"this is last weeks's date: {lw}")

random_date = "Sat 11/20/21 09:43 PM"
random_date_datetime = datetime_date.strptime(random_date, "%a %m/%d/%y %I:%M %p")
print(random_date_datetime)
