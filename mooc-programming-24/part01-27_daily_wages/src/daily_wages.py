# Write your solution here
wage = float(input("Hourly wage:"))
hours = int(input("Hours worked:"))
day = input("Day of the week:")
if day != "Sunday":
    print(f"Daily wages: {wage*hours} euros")
if day == "Sunday":
    print(f"Daily wages: {wage*hours*2} euros")