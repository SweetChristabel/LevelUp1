# Write your solution here
def dict_of_numbers():
    numberionary = {}
    singles = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    singlenary = {}
    for i in range(0, 10):
        singlenary[i] = singles[i]
    teenary = {}
    for i in range(0, 10):
        teenary[i+10] = teens[i]
    tensary = {}
    for ten in range(20, 100, 10):
        tensary[ten] = tens[int(ten/10-2)]
        for i in range (1, 10):
            tensary[ten+i] = f"{tensary[ten]}-{singles[i]}"
    for number, name in singlenary.items():
        numberionary[number] = name
    for number, name in teenary.items():
        numberionary[number] = name
    for number, name in tensary.items():
        numberionary[number] = name
    return numberionary

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])