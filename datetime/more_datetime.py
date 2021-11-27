from datetime import date,time,datetime, timedelta, timezone
from time import timezone

today = date.today()
last_year = date.replace(today, year=today.year-1)
next_year = date.replace(today, year=today.year+1)

covid_start=date(2021,3,15)

current_time = time(17,9,49)
time1 = time.replace(current_time,hour=current_time.hour + 3)

curr_date_time = datetime.now()
# curr_date_time = datetime.now()
what_is_this = datetime.today()

curr_time_stamp = datetime.timestamp(curr_date_time)
curr_utc = datetime.utcfromtimestamp(curr_time_stamp)

new_now = datetime.now(timezone)
print(new_now)