# Write your solution here
while True:
    number = int(input("Please type in a number: "))
    if number > 0:
        fac = 1
        producc = 1
        while fac <= number:
            producc *= fac
            fac += 1
        print(f"The factorial of the number {number} is {producc}")
    else:
        print("Thanks and bye!")
        break