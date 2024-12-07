# Write your solution here
list = []
letter = "b"
while letter != "x":
    print(f"The list is now {list}")
    letter = input("a(d)d, (r)emove or e(x)it: ")
    if letter == "x":
        continue
    if letter == "d":
        if len(list) == 0:
            list.append(1)    
        else:    
            list.append(list[-1]+1)
    if letter == "r":
        list.pop(-1)    
print("Bye!")