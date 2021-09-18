import math

number = float(input("Please type in a number:"))
print("Integer part:", int(number))

decimalPart = math.modf(number)
print("Decimal part:", decimalPart)