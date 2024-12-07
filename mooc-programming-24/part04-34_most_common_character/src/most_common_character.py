# Write your solution here
def most_common_character(word: str):
    rep = 0
    winnernr = 0
    while rep < len(word):
        char = word[rep]
        if word.count(char) > winnernr:
            winnernr = word.count(char)
            winner = char
        rep += 1
    return winner



if __name__ == "__main__":
    word = "whoodissssss"
    print(most_common_character(word))