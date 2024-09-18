# This is a simple weight conversion program

weight = float(input("Enter the weight : "))
unit = input("Kilograms or Pounds (K or L) : ")

if unit == "K":
    weight *= 2.205
    unit = "Lbs"
elif unit == "L":
    weight /= 2.205
    unit = "Kgs"
else:
    print(f"{unit} is not valid!")
    exit()

print(f"Your weight : {round(weight,1)} {unit}")