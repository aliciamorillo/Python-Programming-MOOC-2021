#Please write a program which asks the user for their name and year of birth.
# The program then prints out a message as follows:

name = str(input("What is your name? "))
year = int(input("Which year were you born? "))

futureYears = 2021 - year

print(f"Hi {name}, you will be {futureYears} years old at the end of the year 2021")