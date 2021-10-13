string1 = input("Please type in string 1:")
string2 = input("Please type in string 2:")

length1 = len(string1)
length2 = len(string2)

if length1 > length2:
    print(f"{string1} is longer")
elif length2 > length1:
    print(f"{string2} is longer")
else:
    print("The strings are equally long")