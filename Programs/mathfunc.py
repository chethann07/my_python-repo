# Some of the math functions in python

x = 3.145
y = -3.14
z = 5

# result = round(x)
# result = abs(y)
# result = pow(z,3)
# result = max(x,y,z)
# result = min(x,y,z)

# print(result)

import math

# a = 9
# pi = math.pi
# e = math.e
# squareRoot = math.sqrt(a)
# ceil = math.ceil(x)
# floor = math.floor(x)
# roundFun = round(math.pi,2)

# print(roundFun)

# Calculating circumference of a circle

radius1 = float(input("Enter the radius of a circle : "))
circumference = 2 * math.pi * radius1
print(f"The circumference of a circle is : {round(circumference,2)}")

# Calculating area of a circle

radius2 = float(input("Enter the radius of a circle : "))
area = math.pi * math.pow(radius2, 2)
print(f"The area of a circle is : {round(area,2)}")

# Calculating hypotenuse of a triangle

sideA = float(input("Enter the side A of a triangle : "))
sideB = float(input("Enter the side B of a triangle : "))
c = math.sqrt((math.pow(sideA,2)) + (math.pow(sideB,2)))
print(f"The hypotenuse of a triangle is : {round(c,2)}")