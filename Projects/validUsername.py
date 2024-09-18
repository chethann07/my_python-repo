username = input("Enter the username :")

if len(username) > 12:
    print("Username cant be more than 12 characters")
elif not username.find(" ") == -1:
    print("Username cant have spaces")
elif not username.isalpha(): #isalpha will check for spaces as well 
    print("Username cant contain numbers")
else:
    print(f"Welcome {username}!")

