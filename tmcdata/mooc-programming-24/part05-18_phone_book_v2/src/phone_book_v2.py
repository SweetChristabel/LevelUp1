# Write your solution here
# Write your solution here
cmd = -1
phonebook = {}
while cmd != 3:
    cmd = int(input("command (1 search, 2 add, 3 quit): "))
    if cmd == 1:
        name = input("name: ")
        if name in phonebook:
            for number in phonebook[name]:
                print(number)
        else:
            print("no number")
    elif cmd == 2:
        name = input("name: ")
        number = input("number: ")
        if number == "3":
            break
        if name not in phonebook:
            phonebook[name] = []
        phonebook[name].append(number)
        print("ok!")
    else:
        continue
print("quitting...")