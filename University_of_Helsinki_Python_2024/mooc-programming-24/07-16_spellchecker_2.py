# Write your solution here
wordlist = []
from difflib import get_close_matches
with open("wordlist.txt") as unprocessed_wordlist:
    for line in unprocessed_wordlist:
        wordlist.append(line.strip())

usertext = input("Write text: ")
userwordlist = usertext.split(" ")
returntext = ""
badwordlist = []
for word in userwordlist:
    if word.lower() in wordlist:
        returntext += word+" "
        continue
    else:
        badwordlist.append(word)
        word = "*"+word+"* "
        returntext += word


print(returntext)
if len(badwordlist) > 0:
    print("suggestions:")
    for word in badwordlist:
        sugglist = get_close_matches(word, wordlist)
        print(f"{word}: {', '.join(sugglist)}")

