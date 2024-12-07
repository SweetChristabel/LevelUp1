# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    import string
    with open(filename) as file:
        wordlist = []
        for line in file:
            wordlist += [word.strip(string.punctuation) for word in line.split()]
    return {word: wordlist.count(word) for word in wordlist if wordlist.count(word) >= lower_limit}
        
            
if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 3))