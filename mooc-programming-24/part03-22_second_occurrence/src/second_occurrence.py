# Write your solution here
string = input("Please type in a string: ")
substring = input("Please type in a substring: ")
index = string.find(substring)
rep = 1
while index >= 0 and rep < 2:
    ogindex = index + len(substring)
    string = string [ogindex:]
    index = string.find(substring)
    rep += 1
    if index >= 0:
        print(f"The second occurrence of the substring is at index {ogindex+index}.")
if index == -1:
    print("The substring does not occur twice in the string.")    