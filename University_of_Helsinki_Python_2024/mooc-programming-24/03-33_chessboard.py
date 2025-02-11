# Write your solution here
def chessboard(x):
    def oddrow():
        rep = 1
        while rep <= x:
            if rep % 2 == 1:
                print(1, end="")
                rep += 1
            else:
                print(0, end="")
                rep += 1
        print()
    def evenrow():
        rep = 1
        while rep <= x:
            if rep % 2 == 1:
                print(0, end="")
                rep += 1
            else:
                print(1, end="")
                rep += 1
        print()
    rep = 1
    while rep <= x:
        if rep % 2 == 1:
            oddrow()
            rep += 1
        else:
            evenrow()
            rep += 1
# Testing the function
if __name__ == "__main__":
    chessboard(3)
