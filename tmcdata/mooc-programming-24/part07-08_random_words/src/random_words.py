# Write your solution here

def words(n: int, beginning: str):
    from random import sample
    wordpool = []
    hitlist = []
    with open("words.txt") as wordlist:
        for word in wordlist:
            if word.startswith(beginning):
                wordpool.append(word.strip())
    if n > len(wordpool):
        raise ValueError
    return sample(wordpool, n)




if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)