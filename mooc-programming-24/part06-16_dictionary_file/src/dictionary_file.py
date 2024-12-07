# Write your solution here
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    fun = int(input("Function: "))
    if fun == 1:
        with open("dictionary.txt", "a") as dictionary:
            fin = input("The word in Finnish: ")
            eng = input("The word in English: ")
            dictionary.write(f"{fin} - {eng}\n")
            print("Dictionary entry added")

    if fun == 2:
        with open("dictionary.txt") as dictionary:
            search = input("Search term: ")
            for line in dictionary:
                if search in line:
                    print(line.strip())

    if fun == 3:
        print("Bye!")
        break
    else:
        continue