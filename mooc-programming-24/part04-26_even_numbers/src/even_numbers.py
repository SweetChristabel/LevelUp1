# Write your solution here
def even_numbers(my_list: list):
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print(even_numbers(my_list))