string = input("Please type in a string:")
stringLength = len(string)

asterisk = "*"
asteriskLength = 20 - stringLength

print((asterisk * asteriskLength) + string)