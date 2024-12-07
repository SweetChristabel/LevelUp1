# Write your solution here
def line(x, string):
    if string == "":
        print(x*"*")
    else:
        print(x*(string[0]))

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")
    line(3,"")
    line(6,"o")