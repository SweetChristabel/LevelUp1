# Write your solution here
cafeteria_meals = int(input("How many times a week do you eat at the student cafeteria?"))
cafeteria_price = float(input("The price of a typical student lunch?"))
groceries_week = float(input("How much money do you spend on groceries in a week?"))

print("Average food expenditure:")
print(f"Daily: {(cafeteria_meals*cafeteria_price+groceries_week)/7} euros")
print(f"Weekly: {cafeteria_meals*cafeteria_price+groceries_week} euros")