# Write your solution here
number = int(input("Number: "))
if number % 3 == 0:
    resp3 = "Fizz"
else:
    resp3 = ""
if number % 5 == 0:
    resp5 = "Buzz"
else:
    resp5 = ""
print(f"{resp3}{resp5}")