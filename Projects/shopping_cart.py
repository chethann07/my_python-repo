# This is a shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food you need to buy (q to quit) : ")
    if food.lower() == "q":
        break;
    else:
        foods.append(food)
        price = float(input(f"Enter the price of {food} : ₹"))
        prices.append(price)

print("----- YOUR CART -----")
for food in foods:
    print(f"{food}", end = " ")

print() 

for price in prices:
    total += price

print(f"The total price of your cart is : ${total}")



