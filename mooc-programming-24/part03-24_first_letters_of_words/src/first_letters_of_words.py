# Write your solution here
sentence = input("Please type in a sentence: ")
index = sentence.find(" ")
while index > -1:
    print(sentence[0])
    sentence = sentence[index+1:]
    index = sentence.find(" ")
print(sentence[0])