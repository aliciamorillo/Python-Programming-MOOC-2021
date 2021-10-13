limit = int(input("Limit:"))
sum = 0
x = 0
printNumbers = ""

while sum < limit:
    x += 1
    sum += x
    printNumbers += " + " + str(x)

length = len(printNumbers)
newString = printNumbers[2:length]

print(f"The consecutive sum:{newString} = {sum}")