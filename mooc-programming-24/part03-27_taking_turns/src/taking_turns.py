# Write your solution here
number = int(input("Please type in a number: "))
backend = 1
frontend = number
while backend <= (number+1)/2:
    print(backend)
    if backend == frontend:
        break
    print(frontend)
    backend += 1
    frontend -= 1
