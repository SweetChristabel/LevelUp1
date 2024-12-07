# Write your solution here
word = input("Word: ")
print(30*"*")
if len(word)%2 == 0:
    spaces = int(14-len(word)/2)
    print("*"+" "*spaces+word+" "*spaces+"*")
else:
    spaces = int(14-(len(word)-1)/2)
    print("*"+" "*(spaces-1)+word+" "*spaces+"*")
print(30*"*")