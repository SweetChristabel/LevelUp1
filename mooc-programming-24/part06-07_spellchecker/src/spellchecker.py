# write your solution here
wordlist = []
with open("wordlist.txt") as unprocessed_wordlist:
    for line in unprocessed_wordlist:
        wordlist.append(line.strip())

usertext = input("Write text: ")
userwordlist = usertext.split(" ")
returntext = ""
for word in userwordlist:
    if word.lower() in wordlist:
        returntext += word+" "
        continue
    else:
        word = "*"+word+"* "
        returntext += word


print(returntext)