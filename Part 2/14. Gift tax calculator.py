valueGift = int(input("Value of gift:"))

if valueGift < 5000:
    print("No tax!")

elif valueGift >= 5000 and valueGift < 25000:
    amount = 100 + (valueGift - 5000) * 0.08
    print("Amount of tax:", amount)

elif valueGift >= 25000 and valueGift < 55000:
    amount = 1700 + (valueGift - 25000) * 0.10
    print("Amount of tax:", amount)

elif valueGift >= 55000 and valueGift < 200000:
    amount = 4700 + (valueGift - 55000) * 0.12
    print("Amount of tax:", amount)

elif valueGift >= 200000 and valueGift < 1000000:
    amount = 22100 + (valueGift - 200000) * 0.15
    print("Amount of tax:", amount)

elif valueGift >= 1000000:
    amount = 142100 + (valueGift - 1000000) * 0.17
    print("Amount of tax:", amount)