# Write your solution here
cmd = -1
phonebook = {}
while cmd != 3:
    cmd = int(input("command (1 search, 2 add, 3 quit): "))
    if cmd == 1:
        name = input("name: ")
        if name in phonebook:
            print(phonebook[name])
        else:
            print("no number")
    elif cmd == 2:
        name = input("name: ")
        number = input("number: ")
        if number == "3":
            break
        phonebook[name] = number
        print("ok!")
    else:
        continue
print("quitting...")