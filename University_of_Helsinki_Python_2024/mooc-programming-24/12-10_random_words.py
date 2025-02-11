# Write your solution here:
def word_generator(characters:str, length: int, amount: int):
    import random
    rep = 0
    while rep < amount:
        yield "".join(random.choices(characters, k= length))
        rep += 1

if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)