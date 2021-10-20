string = input("Please type in a string:")
word = "";

for x in string[::-1]:
    word += x
    reversedstring=''.join(reversed(word))
    print(reversedstring)
