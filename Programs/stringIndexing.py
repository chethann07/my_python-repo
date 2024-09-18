# indexing -> acccessing elements of sequence using [] (indexing operator)
# string[start : end : step]

creditcard_number = "1234-5678-9012-3456"

# print(creditcard_number[0])
# print(creditcard_number[0:10])
# print(creditcard_number[:10])
# print(creditcard_number[3:])
# print(creditcard_number[::2])
# print(creditcard_number[-1])

# to reverse a string
print(creditcard_number[::-1])

# to access last 4 digits of a string
print(f"XXXX-XXXX-XXXX-{creditcard_number[-4:]}")