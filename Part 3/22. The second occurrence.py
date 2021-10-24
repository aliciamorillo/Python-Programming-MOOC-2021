string = input("Please type in a string:")
substring = input("Please type in a substring:")

substringLength = len(substring)

index1 = string.find(substring)

index2 = string.find(substring, index1+substringLength)

if index2 != -1:
    print(f"The second occurrence of the substring is at index {index2}.")
else:
    print("The substring does not occur twice in the string.")