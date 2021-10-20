word = input("Please type in a word:")
character = input("Please type in a character:")

index = word.find(character)

if len(word[index:index+3]) == 3:
    print(word[index:index+3])