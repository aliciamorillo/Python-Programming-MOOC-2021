while True:
    number = int(input("Please type in a number:"))
    if number <= 0:
        print("Thanks and bye!")
        break

    factorial = 1

    for i in range(1,number + 1):    
        factorial = factorial*i    
    print("The factorial of the number ",number,"is",factorial)    