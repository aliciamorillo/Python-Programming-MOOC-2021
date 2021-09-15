#Please write a program which asks the user for two numbers and an operation.
#If the operation is add, multiply or subtract, the program should calculate and print out the result of the operation with the given numbers. 

number1 = int(input("Number 1:"))
number2 = int(input("Number 2:"))
operation = input("Operation:")

if operation == "add":
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")

if operation == "subtract":
    result = number1 - number2
    print(f"{number1} - {number2} = {result}")

if operation == "multiply":
    result = number1 * number2
    print(f"{number1} * {number2} = {result}")