    # Write your solution here

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    fun = int(input("Function: "))
    if fun == 0:
        print("Bye now!")
        break
    if fun == 1:
        with open("diary.txt", "a") as diary:
            entry = input("Diary entry: ")
            diary.write(entry+"\n")
            print("Diary saved")
            print()
    if fun == 2:
        with open("diary.txt") as diary:
            print("Entries:")
            for line in diary:
                print(line.strip())
    else:
        continue