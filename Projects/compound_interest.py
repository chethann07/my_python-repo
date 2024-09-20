# This program calculates the compound interest:
    # A = P(1 + (R/N))^ T
    # A -> Total amount
    # P -> Principle amount
    # R -> Rate of interest
    # T -> Time period elapsed in years

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount : "))
    if principle < 0:
        print("Principle amount cannot be less than zero.")
    else:
        break

while True:
    rate = float(input("Enter the rate of interest : "))
    if rate < 0:
        print("Rate of interest cannot be less than zero.")
    else:
        break

while True:
    time = int(input("Enter the time in years : "))
    if time < 0:
        print("Time cannot be less than zero.")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"The balance after {time} year/s is : ${total:.2f}")



