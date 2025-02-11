# Write your solution here
def length_of_longest(my_list: list):
    winner = 0
    for i in my_list:
        if len(i) > winner:
            winner = len(i)
    return winner


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    print(length_of_longest(my_list))