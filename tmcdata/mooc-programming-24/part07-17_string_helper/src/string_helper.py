# Write your solution here
def change_case(orig_string: str):
    import string
    newstring = ""
    oldstring = list(orig_string)
    for i in oldstring:
        l = ""
        if i in string.ascii_lowercase:
            l = i.upper()
        elif i in string.ascii_uppercase:
            l = i.lower()
        else:
            l = i
        newstring += l
    return newstring

def split_in_half(orig_string: str):
    if len(orig_string) % 2 == 0:
        index = int(len(orig_string)/2)
    else:
        index = int(len(orig_string)/2)
    return orig_string[:index], orig_string[index:]

def remove_special_characters(orig_string: str):
    import string
    newstring = ""
    oldstring = list(orig_string)
    for i in oldstring:
        if i in string.ascii_letters or i in string.digits or i == " ":
            newstring += i
    return newstring

if __name__ == "__main__":
    print(change_case("Well hello therE!"))
    p1, p2 = split_in_half("abcd")
    print(p1)
    print(p2)
    print(remove_special_characters("This is a test, lets see how it goes!!!11!"))
    