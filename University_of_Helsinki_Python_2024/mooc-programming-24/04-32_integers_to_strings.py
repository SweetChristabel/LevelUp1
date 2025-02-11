# Write your solution here
def formatted(my_list: list):
    new_list = []
    for i in my_list:
        i = f"{i:.2f}"
        new_list.append(i)
    return new_list

if __name__ == "__main__":
    floaters = [1.234, 0.333, 0.11111, 3.446]
    print(formatted(floaters))