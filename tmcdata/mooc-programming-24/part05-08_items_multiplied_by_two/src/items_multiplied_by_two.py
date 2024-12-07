# Write your solution here
def double_items(numbers: list):
    doubled = []
    for i in numbers:
        doubled.append(i*2)
    return doubled



if __name__ == "__main__":
    numboopsters = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numboopsters)
    print("original:", numboopsters)
    print("doubled:", numbers_doubled)