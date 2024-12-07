# Write your solution here
def first_word(sentence):
    index = sentence.find(" ")
    return sentence[0:index]

def second_word(sentence):
    index = sentence.find(" ")
    sentence = sentence[index+1:]
    index = sentence.find(" ")
    if index < 0:
        return sentence
    else:
        return sentence[0:index]

def last_word(sentence):
    index = 0
    while index >= 0:
        sentence = sentence[index+1:]
        index = sentence.find(" ")
    return sentence
        


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
    sentence = "a quick brown fox jumped over the lazy dog"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))