word = input("Please type in a word:")
character = input("Please type in a character:")

for i in range(len(word)):
    if word[i] == character and len(word[i:i+3]) == 3:
        print(word[i:i+3])