# while loop -> executes the loop until the given condition inside the loop is true

# Example 1
name = input("Enter your name : ")
while name == "":
   print("Name cannot be empty")
   name = input("Enter your name : ") 
print(f"Hello {name}")

# Example 2
food = input("Enter your fav food and press q to quit : ")
while not food == "q":
   print(f"You like {food}")
   food = input("Enter your another fav food and press q to quit : ")
print("bye")