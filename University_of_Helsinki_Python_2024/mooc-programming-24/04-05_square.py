# Copy here code of line function from previous exercise
def line(x, string):
    if string == "":
        print(x*"*")
    else:
        print(x*(string[0]))

def square(size, character):
    # You should call function line here with proper parameters
    rep = 1
    while rep <= size:
        line(size, character)
        rep +=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")