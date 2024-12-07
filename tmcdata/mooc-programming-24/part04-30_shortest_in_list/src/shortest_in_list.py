# Write your solution here
def shortest(my_list: list):
    length = len(my_list[0])
    winner = my_list[0]
    for i in my_list:
        if len(i) < length:
            length = len(i)
            winner = i
    return winner        


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    print(shortest(my_list))