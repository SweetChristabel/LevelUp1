# Write your solution here
def generate_strong_password(length: int, nr: bool, spec: bool):
    import random
    from string import ascii_lowercase, digits
    special_characters = "!?=+-()#"
    charpool = list(ascii_lowercase)
    pwpool = []
    pwpool.append(random.choice(charpool))
    randomlength = length - 1
    if nr == True:
        pwpool.append(random.choice(digits))
        charpool += digits
        randomlength -= 1
    if spec == True:
        pwpool.append(random.choice(special_characters))
        charpool += special_characters
        randomlength -=1
    for ltr in random.sample(charpool, randomlength):
        pwpool.append(ltr)
    random.shuffle(pwpool)
    password = ""
    for ltr in pwpool:
        password += str(ltr)
    return password
    
if __name__ == "__main__":
    print(generate_strong_password(10,True,True))
    print(generate_strong_password(8, False, True))
    print(generate_strong_password(6, True, False))
    print(generate_strong_password(7, False, False))