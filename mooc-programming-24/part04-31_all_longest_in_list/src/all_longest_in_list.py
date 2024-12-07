# Write your solution here
def all_the_longest(my_list: list):
    listoflongest = []
    length = 0
    for i in my_list:
        if len(i) > length:
            listoflongest = []
            listoflongest.append(i)
            length = len(i)
        elif len(i) == length:
            listoflongest.append(i)
    return listoflongest

if __name__ == "__main__":
    nameronies = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    print(all_the_longest(nameronies))