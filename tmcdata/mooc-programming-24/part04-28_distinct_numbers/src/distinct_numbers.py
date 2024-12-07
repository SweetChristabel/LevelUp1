# Write your solution here
def distinct_numbers(my_list: list):
    output = []
    for i in my_list:
        if i in output:
            continue
        else:
            output.append(i)
    return sorted(output)

if __name__ == "__main__":
    numberonies = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(numberonies))