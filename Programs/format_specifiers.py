#format specifiers {vlaue:flag} -> these format a value based on the flags written

price1 = 26838.6541
price2 = -123.45
price3 = 12345.8998

# .(number)f -> round to that many decimal places
print(f"{price1:.3f}")
print(f"{price2:.3f}")
print(f"{price3:.3f}")
print()
# (number) -> allocate that many spaces
print(f"{price1:15}")
print(f"{price2:15}")
print(f"{price3:15}")
print()
# 0(number) -> allocate 0 pad and number amount of spaces
print(f"{price1:015}")
print(f"{price2:015}")
print(f"{price3:015}")
print()
# <(number) -> left justify
print(f"{price1:<15}")
print(f"{price2:<15}")
print(f"{price3:<15}")
print()
# >(number) -> right justify
print(f"{price1:>15}")
print(f"{price2:>15}")
print(f"{price3:>15}")
print()
# ^(number) -> centre align
print(f"{price1:^15}")
print(f"{price2:^15}")
print(f"{price3:^15}")
print()
# + -> insert + before positive values
print(f"{price1:+}")
print(f"{price2:+}")
print(f"{price3:+}")
print()
# ' ' -> insert a space  before positive values
print(f"{price1: }")
print(f"{price2: }")
print(f"{price3: }")
print()
# , -> comma separator
print(f"{price1:,}")
print(f"{price2:,}")
print(f"{price3:,}")
print()


