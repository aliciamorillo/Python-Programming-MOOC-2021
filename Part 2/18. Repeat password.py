password1 = input("Password:")

while True:
    password2 = input("Repeat password:")

    if password1 == password2:
        print("User account created!")
        break

    if password1 != password2:
        print("They do not match!")