import datetime

date = datetime.date(2025, 1, 2) # for custom date and time
today = datetime.date.today() # for getting today's date

time = datetime.time(12, 30, 0)
now = datetime.datetime.now() #printing system time


now = now.strftime("%H:%M:%S %d-%m-%Y") # these are the format specifiers which we can get from the official documentation of datetime module
print(now)



# if current date and time passes a target date and time

target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has NOT passed")
