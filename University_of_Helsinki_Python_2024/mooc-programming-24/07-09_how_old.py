# Write your solution here
from datetime import datetime, timedelta
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
millennium = datetime(1999, 12, 31)
birthday = datetime(year, month, day)
difference = millennium - birthday
if difference.days < 0:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {difference.days} days old on the eve of the new millennium.")