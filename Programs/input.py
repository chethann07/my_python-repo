# input() -> prompts the user to enter the data

name = input("Enter your name :")
age = int(input("Enter your age :"))

print(f"Your name is {name} and you are {age} years old")

#Exercise 1 : Calculating the area of a rectangle

#formula : area = length * width

length = float(input("Enter the length :"))
width = float(input("Enter the width :"))
area = length * width

print(f"The area of the rectangle is {area}")

#Exercise 2 : Shopping cart problem

item = input("What item would you like to buy? : ")
price = float(input(f"What is the price of the {item}? : "))
quantity = int(input(f"Enter the number of {item} you need? : "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is ${total}")