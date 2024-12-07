# Write your solution here
string = input("Please type in a string: ")
length = 1
while len(string)>= length:
    print(string[-length:])
    length += 1
