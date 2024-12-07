# Write your sold
def read_input(prompt: str, min: int, max: int):
    while True:
        try:
            inp = int(input(prompt))
            if inp > min and inp < max:
                return inp
        except ValueError:
            pass
        print(f"You must type in an integer between {min} and {max}")







if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)