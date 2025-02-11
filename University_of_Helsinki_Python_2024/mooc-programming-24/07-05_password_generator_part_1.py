# Write your solution here
def generate_password(length: int):
    from string import ascii_lowercase, digits
    from random import shuffle
    pool = list(ascii_lowercase)
    shuffle(pool)
    password = ""
    for ltr in pool[:length]:
        password += ltr
    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))