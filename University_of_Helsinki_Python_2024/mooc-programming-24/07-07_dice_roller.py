# Write your solution here

#This code would've been optimal and enables for reuse, but alas, the exercise asks for a different approach.

#dies = {}
#dies["A"] = (3, 3, 3, 3, 3, 6)
#dies["B"] = (2, 2, 2, 5, 5, 5)
#dies["C"] = (1, 4, 4, 4, 4, 4)
import random
#
#def roll(die:str):
#    return random.choice(dies[die])

def roll(die:str):
    if die == "A":
        chosendie = (3, 3, 3, 3, 3, 6) 
    if die == "B":
        chosendie = (2, 2, 2, 5, 5, 5)
    if die == "C":
        chosendie = (1, 4, 4, 4, 4, 4)
    return random.choice(chosendie)

def play(die1:str, die2:str, times: int):
    win1 = 0
    win2 = 0
    ties = 0
    for i in range(times):
        roll1 = roll(die1)
        roll2 = roll(die2)
        if roll1 > roll2:
            win1 += 1
        elif roll1 < roll2:
            win2 += 1
        else:
            ties += 1
    return win1, win2, ties


if __name__ == "__main__":
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)