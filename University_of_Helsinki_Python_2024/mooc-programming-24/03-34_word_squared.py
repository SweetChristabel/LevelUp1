# Write your solution here
def squared(string, x):
    rep1 = 1
    index = 0
    while rep1 <= x:
        rep = 1
        while rep <= x:
            if index >= len(string):
                index = 0
            print(string[index], end="")
            rep += 1
            index += 1
        print()
        rep1 += 1
if __name__ == "__main__":
    squared("whodis", 5)