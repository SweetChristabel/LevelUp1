# Write your solution here
from datetime import datetime, timedelta
file = input("Filename: ")
startdate = input("Starting date: ")
startdate = startdate.split(".")
oneday = timedelta(days = 1)
startdate = datetime(int(startdate[2]), int(startdate[1]), int(startdate[0]))
amtofdays = int(input("How many days: "))
total = 0
screentime = {}
print("Please type in screen time in minutes on each day (TV computer mobile): ")
for day in range(amtofdays):
    date = (startdate+day*oneday)
    scrtimeofday = input(f"Screen time {date.strftime('%d.%m.%Y')}: ")
    scrtimeofday = scrtimeofday.split(" ")
    scrtimelist = []
    for i in scrtimeofday:
        scrtimelist.append(int(i))
    screentime[date.strftime('%d.%m.%Y')] = scrtimelist
    total += sum(scrtimelist)
print(screentime)
with open(file, "w") as file:    
    file.write(f"Time period: {startdate.strftime('%d.%m.%Y')}-{(startdate+timedelta(days = amtofdays-1)).strftime('%d.%m.%Y')}\n")
    file.write(f"Total minutes: {total}\n")
    file.write(f"Average minutes: {total/amtofdays}\n")
    for day in screentime:    
        file.write(f"{day}: {screentime[day][0]}/{screentime[day][1]}/{screentime[day][2]}\n")
