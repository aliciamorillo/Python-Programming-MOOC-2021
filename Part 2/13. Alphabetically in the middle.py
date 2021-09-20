letter1 = input("1st letter:")
letter2 = input("2nd letter:")
letter3 = input("3rd letter:")

word = letter1 + letter2 + letter3

def sortString(str):
    return ''.join(sorted(str))

sortedWord = sortString(word)

print("The letter in the middle is", sortedWord[1])