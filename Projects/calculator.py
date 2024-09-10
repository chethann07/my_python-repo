# This is a simple calculator using python

operator = input("Enter the operator which you need (+ - * /) : ")
num1 = float(input("Enter the number1 : "))
num2 = float(input("Enter the number2 : "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Enter a valid operator!")
    exit()

print(result)