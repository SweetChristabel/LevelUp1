# Write your solution here
def palindromes(word) -> str:
    wordlist = list(word)
    tsildrow = list()
    for i in wordlist:
        tsildrow.insert(0,i)
    if wordlist == tsildrow:
        return True
    else:
        return False

while True:
    word = input("Please type in a palindrome: ")
    if palindromes(word) == True:
        break
    else:
        print("that wasn't a palindrome")
print(f"{word} is a palindrome!")

    

