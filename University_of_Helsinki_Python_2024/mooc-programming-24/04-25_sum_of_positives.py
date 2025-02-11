# Write your solution here
def sum_of_positives(inputlist) -> list:
    positives = []
    for i in inputlist:
        if i > 0:
            positives.append(i)
    return sum(positives)


if __name__ == "__main__":
    my_list = [-9, -7, -5, -2, 0, 1, 3, 5, 7, 5]
    print(sum_of_positives(my_list))