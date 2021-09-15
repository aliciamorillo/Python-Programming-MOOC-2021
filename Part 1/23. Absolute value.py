#Please write a program which asks the user for an integer number. 
# If the number is less than zero, the program should print out the number multiplied by -1. 
# Otherwise the program prints out the the number as is
number = int(input("Please type in a number: "))

if number < 0:
    newNumber = number * -1
    print(f"The absolute value of this number is {newNumber}")
elif number >= 0:
    print(number)