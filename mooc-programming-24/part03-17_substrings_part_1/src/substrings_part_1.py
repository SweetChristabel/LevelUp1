# Write your solution here
string = input("Please type in a string: ")
length = len(string)+1
rep = 1
while rep <= length:
    print(string[:rep-1])
    rep += 1