string = input("Please type in a string:")
length = len(string)

secondChar = string[1]
secondLastChar = string[length - 2]

if secondChar == secondLastChar:
    print(f"The second and the second to last characters are {secondChar}")
else:
    print("The second and the second to last characters are different")