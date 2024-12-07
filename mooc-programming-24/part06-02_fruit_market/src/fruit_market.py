# write your solution here
def read_fruits():
    fruitionary = {}
    with open("fruits.csv") as fruitfile:
        for line in fruitfile:
            pairs = line.split(";")
            fruitionary[pairs[0]] = float(pairs[1])
    return fruitionary

if __name__ == "__main__":
    print(read_fruits())