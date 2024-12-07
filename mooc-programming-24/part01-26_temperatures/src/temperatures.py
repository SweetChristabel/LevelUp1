# Write your solution here
tempF = int(input("Please type in a temperature (F):"))
tempC = (5/9)*(tempF-32)
print(f"{tempF} degrees Fahrenheit equals {tempC} degrees Celsius")
if tempC < 0:
    print("Brr! It's cold in here!")