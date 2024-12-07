# Write your solution here
rep = int(input("How many items: "))
list = []
rep1 = 0
while rep > 0:
    rep1 += 1
    list.append(int(input(f"Item {rep1}:")))
    rep -= 1
print (list)