# Write your solution here
story = ""
lastword = "null"
while True:
    word = input("Please type in a word:")
    if word == lastword or word == "end":
        break
    story += word + " "
    lastword = word
print(story)
    