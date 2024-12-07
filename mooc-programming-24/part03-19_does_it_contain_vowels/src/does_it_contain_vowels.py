# Write your solution here
string = input("Please type in a string")
vowels = "aeo"
index = 0
while index < len(vowels):
    if vowels[index] in string:
        print(vowels[index]+" found")
    else:
        print(vowels[index]+" not found")
    index += 1