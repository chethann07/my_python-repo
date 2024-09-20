# while loop -> executes a block of code a fixed number of times

# Example 1 
for i in range(1,11):
    print(i, end = " " )

print()

# Example 2 
for i in reversed(range(1,11)):
    print(i, end = " " )

print()

# Example 3 
for i in range(1,21):
    if i == 13:
        continue
    else:
        print(i, end = " " )

print()

# Example 4 
credit_card = "1234-5678-9012-3456"
for i in credit_card:
    print(i, end = " " )

print()

# Example 5
for i in range(1,11,2):
    print(i, end = " " )
