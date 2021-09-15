#Please write a program for solving a quadratic equation of the form ax²+bx+c. The program asks for values a, b and c. 
# It should then use the quadratic formula to solve the equation.

from math import sqrt

valueA = int(input("Value of a:"))
valueB = int(input("Value of b:"))
valueC = int(input("Value of c:"))

d = (valueB**2) - (4*valueA*valueC)

sol1 = (-valueB-sqrt(d))/(2*valueA)
sol2 = (-valueB+sqrt(d))/(2*valueA)

print("The roots are", sol1, "and", sol2)