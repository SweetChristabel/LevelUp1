# Write your solution here
def histogram(word: str):
    letters = {}
    for i in range(0, len(word)):
        ltr = word[i]
        if ltr not in letters:
            letters[ltr]=0
        letters[ltr] += 1
    for key, value in letters.items():
        print(key + " " + value * "*")

if __name__ == "__main__":
    histogram("statistically")