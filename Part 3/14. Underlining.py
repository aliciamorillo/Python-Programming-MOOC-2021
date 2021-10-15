while True:
    string = input("Please type in a string:")
    length = len(string)

    print(string)
    print("-" * length)

    if string == "":
        break