# Write your solution here
string = input("Please type in a word: ")
char = input("Please type in a character: ")
char_index = string.find(char)
substring = string[char_index:char_index+3]
if len(string)>= char_index+3:
    print(substring)