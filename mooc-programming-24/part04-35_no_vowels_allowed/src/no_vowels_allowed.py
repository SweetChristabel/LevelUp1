# Write your solution here
def no_vowels(sentence: str):
    listavowels = ["a", "e", "i", "o", "u"]
    listaletters = []
    sntnc = ""
    rep = 0
    while rep < len(sentence): #To future Simona potentially consulting this code - You could've just done a list(sentence) here and spared yourself the loop :))))))
        if not sentence[rep] in listavowels:
            listaletters.append(sentence[rep])
        rep += 1

    for i in listaletters:
        sntnc += str(i)
    return sntnc

if __name__ == "__main__":
    sentence = "To a list and back to string"
    print(no_vowels(sentence))