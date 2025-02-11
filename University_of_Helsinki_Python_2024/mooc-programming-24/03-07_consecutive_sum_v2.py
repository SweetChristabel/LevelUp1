# Write your solution here
number = 1
addition = 1
limit = int(input("Limit: "))
string = f"The consecutive sum: {addition}"
while number < limit:
    addition += 1
    number += addition
    string += f" + {addition}"
string += f" = {number}"
print(string)