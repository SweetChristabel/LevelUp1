# Copy here code of line function from previous exercise
def line(x, string):
    if string == "":
        print(x*"*")
    else:
        print(x*(string[0]))

def box_of_hashes(height):
    # You should call function line here with proper parameters
    rep = 1
    while rep <= height:
        line(10, "#")
        rep+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
