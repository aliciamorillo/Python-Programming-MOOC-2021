#Please write a program which asks for the hourly wage, hours worked, and the day of the week. 
# The program should then print out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.

hourlyWage = float(input("Hourly wage:"))
hoursWorked = float(input("Hours worked:"))
day = input("Day of the week:")

wage = hourlyWage * hoursWorked

if day == "Sunday":
    double = wage * 2
    print(f"Daily wages: {double} euros")

elif day != "Sunday":
    print(f"Daily wages: {wage} euros")