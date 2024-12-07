# Write your solution here
def separate_characters(my_string: str):
    import string
    ascii = ""
    punct = ""
    rest = ""
    for i in list(my_string):
        if i in string.ascii_letters:
            ascii += i
        elif i in string.punctuation:
            punct += i
        else:
            rest += i
    return ascii, punct, rest



if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])