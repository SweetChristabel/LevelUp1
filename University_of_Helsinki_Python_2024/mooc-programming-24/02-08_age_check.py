# Write your solution here
age = int(input("What is your age? "))
if age > 4 and age < 122:
    print(f"Ok, you're {age} years old")
elif age >= 0 and age < 5:
    print("I suspect you can't write quite yet...")
else:
    print("That must be a mistake")