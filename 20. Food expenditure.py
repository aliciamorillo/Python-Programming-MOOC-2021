#Please write a program which estimates a user's typical food expenditure.

timesEat = int(input("How many times a week do you eat at the student cafeteria?"))
price = float(input("The price of a typical student lunch?"))
money = float(input("How much money do you spend on groceries in a week?"))

daily = (money + (timesEat * price)) / 7
weekly = money + (timesEat * price)

answer = str(round(daily, 2))

print("Average food expenditure:")
print(f"Daily: {answer} euros")
print(f"Weekly: {weekly} euros")