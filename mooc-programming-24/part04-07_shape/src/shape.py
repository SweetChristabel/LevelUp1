# Copy here code of line function from previous exercise and use it in your solution
def line(x, string):
    if string == "":
        print(x*"*")
    else:
        print(x*(string[0]))

def triangle(width, a):
# make a triangle
    rep = 1
    while rep <= width:
        line(rep, a)
        rep += 1

def box(width, height, b):
# make a box
    rep = 1
    while rep <= height:
        line(width, b)
        rep +=1

def shape(width, a, height, b):
    triangle(width, a)
    box(width, height, b)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")