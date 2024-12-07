# write your solution here
def largest():
    with open("numbers.txt") as my_file:
        largest = int(max(my_file))
    return largest


if __name__ == "__main__":
    print(largest())
