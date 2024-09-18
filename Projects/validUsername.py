# A valid username is the one which has the following:
# 1. Character count must not be greater than 12
# 2. Username must not contain any spaces
# 3. Username must not containt any numbers

username = input("Enter the username :")

if len(username) > 12:
    print("Username cant be more than 12 characters")
elif not username.find(" ") == -1:
    print("Username cant have spaces")
elif not username.isalpha(): #isalpha will check for spaces as well 
    print("Username cant contain numbers")
else:
    print(f"Welcome {username}!")

