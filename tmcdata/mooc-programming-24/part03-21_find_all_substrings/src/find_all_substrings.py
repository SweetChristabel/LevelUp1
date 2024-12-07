# Write your solution here
word = input("Please type in a word: ")
char = input("Please type in a character: ")
index = 1
index = word.find(char)
while index >= 0:
    if len(word) >= index+3:
        print(word[index:index+3])
    word = word[index+1:]
    index = word.find(char)