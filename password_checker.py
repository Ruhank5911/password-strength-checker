password = input("Enter a test password: ")

if len(password) < 8:
    print("Weak password")
elif len(password) < 12:
    print("Moderate password")
else:
    print("Strong password")
