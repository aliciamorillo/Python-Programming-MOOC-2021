number = int(input("Please type in a number: "))
index = 1

while index <= number:
    for f in range(1,number+1):
        print(f'{index} x {f} = {index * f}')
    index += 1