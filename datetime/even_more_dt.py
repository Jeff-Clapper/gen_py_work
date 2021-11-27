from datetime import date, time, datetime,timedelta

now = datetime.now()
today_date_str = datetime.strftime(now,"%A, %B %d, %Y.")
current_time_str = datetime.strftime(now,"%I:%M %p")

print(f"Today is {today_date_str}")
print(f"The time is now {current_time_str}")

tomorrow = datetime(2021,11,28)

print(f"Tomorrow's date is {tomorrow.strftime('%m/%d/%Y')}")

time_remaining = tomorrow - now
print(f'time between now and tomorrow this time is {time_remaining}')