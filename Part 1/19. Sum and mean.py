#Please write a program which asks the user for four numbers. 
# The program then prints out the sum and the mean of the numbers.

number1 = int(input("Number 1:"))
number2 = int(input("Number 2:"))
number3 = int(input("Number 3:"))
number4 = int(input("Number 4:"))

sum = number1 + number2 + number3 + number4
mean = (number1 + number2 + number3 + number4) / 4

print(f"The sum of the numbers is {sum} and the mean is {mean}")