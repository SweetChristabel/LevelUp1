
def balanced_brackets(my_string: str):
    bracketsonly = ""
    for char in my_string:
        if char in "()[]":
            bracketsonly += char  
    print(bracketsonly)
    if len(bracketsonly) == 0:
        return True
    if bracketsonly[0] == '(' and bracketsonly[-1] == ')':
        pass
    elif bracketsonly[0] == '[' and bracketsonly[-1] == ']':
        pass
    else:
        return False

    # remove first and last character
    return balanced_brackets(bracketsonly[1:-1])

if __name__ == "__main__":
    ok = balanced_brackets("([([])])")
    print(ok)

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("square[brackets]")
    print(ok)

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)