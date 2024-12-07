# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.numcount = 0
        self.numlist = []

    def add_number(self, number:int):
        self.numlist.append(number)


    def count_numbers(self):
        return len(self.numlist)
    
    def get_sum(self):
        return sum(self.numlist)
    
    def average(self):
        if len(self.numlist) != 0:
            return sum(self.numlist)/len(self.numlist)
        else:
            return 0

statistics = NumberStats()
odds = NumberStats()
evens = NumberStats()
userinp = 0
print("Please type in integer numbers:")
while True:
    userinp = int(input(""))
    if userinp == -1:
        break
    statistics.add_number(userinp)

    if userinp % 2 == 0:
        evens.add_number(userinp)
    else:
        odds.add_number(userinp)


print(f"Sum of numbers: {statistics.get_sum()}")
print(f"Mean of numbers: {statistics.average()}")
print(f"Sum of even numbers: {evens.get_sum()}")
print(f"Sum of odd numbers: {odds.get_sum()}")