# Write your solution here
def spruce(x):
    rep = 1
    space = x-1
    print("a spruce!")
    while rep <= x:
        print(space*" "+(2*rep-1)*"*")
        rep += 1
        space -= 1
    print ((x-1)*" "+"*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
    print()
    spruce(10)
    print()
    spruce(3)