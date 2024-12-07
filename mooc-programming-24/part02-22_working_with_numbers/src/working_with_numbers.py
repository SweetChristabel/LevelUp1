# Write your solution here
print ("Please type in integer numbers. Type in 0 to finish.")
amt= 0
tot = 0
pos = 0
neg = 0
while True:
    num = int(input("Number:"))
    if num == 0:
        break
    elif num > 0:
        pos += 1
    else:
        neg += 1
    amt += 1
    tot += num
print ("Numbers typed in", amt)
print ("The sum of the numbers is", tot)
print ("The mean of the numbers is", tot/amt)
print (f"Positive numbers {pos}\nNegative numbers {neg}")
