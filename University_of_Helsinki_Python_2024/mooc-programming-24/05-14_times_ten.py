# Write your solution here
def times_ten(start_index: int, end_index: int):
    simonasbigdicctionary = {}
    numberange = range(start_index, end_index+1)
    for i in numberange:
        simonasbigdicctionary[i] = i*10
    return simonasbigdicctionary

if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)
