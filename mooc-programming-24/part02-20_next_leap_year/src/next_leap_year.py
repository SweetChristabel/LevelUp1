# Write your solution here
year= int(input("Year:"))
if year % 4 == 0:
    nextleap = year + 4
else:
    nextleap = year + (4 - year % 4)
if nextleap % 100 == 0:
    if nextleap % 400 != 0:
        nextleap +=4
print(f"The next leap year after {year} is {nextleap}")