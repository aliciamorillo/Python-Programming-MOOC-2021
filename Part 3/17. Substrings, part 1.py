string = input("Please type in a string:")
index = "";

for x in string:
    index += x
    print(string[0:len(index)])