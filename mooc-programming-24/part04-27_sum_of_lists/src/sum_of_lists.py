# Write your solution here
def list_sum(a, b):
    listofsums = []
    y = 0
    for i in a:
        listofsums.append(i+b[y])
        y += 1
    return listofsums


if __name__ == "__main__":
    a = [10, 10, 10, 11]
    b = [99, 999, 9, 99]
    print (list_sum(a, b))