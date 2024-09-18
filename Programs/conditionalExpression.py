# Conditional expression is a one line shortcut for if-else statements (ternary operators)

a = 10
b = 98
c = 1028

max_num = a if a > b else b
min_num = a if a < b else b
even_odd = "Even" if c % 2 == 0 else "Odd"

print(max_num)
print(min_num)
print(even_odd)