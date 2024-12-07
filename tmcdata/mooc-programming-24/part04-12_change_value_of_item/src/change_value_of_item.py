# Write your solution here
list = [1, 2, 3, 4, 5]
index = 0
while index != -1:
    index = int(input("Index: "))
    if index == -1:
        continue
    newvalue = int(input("New value: "))
    list[index] = newvalue
    print(list)