# Collections -> a single "variable" used to store multiple values

# List = [] -> they are ordered and mutable, duplicates are allowed and any type of data can be stored

fruits = ["apple", "banana", "pineapple", "orange", 1]
# print(help(fruits)) # To get built-in methods
# fruits[0] = "chikoo" # This means they are mutable

# To iterate through the loop
# for fruit in fruits:
#     print(fruit, end = " ")

# print(len(fruits))
# print(fruits.count("banana"))
# fruits.sort()
# fruits.reverse()
# fruits.pop()
# fruits.append("chikoo")
# print("apple" in fruits)
# fruits.clear()
# fruits.insert(2, "kangaroo")

# print(fruits)



# Set = {} -> they are unordered and immutable any type of data can be stored

animals = {"elephant", "kangaroo", "giraffe", "lion", "elephant", 1}
# print(help(animals)) # To get built-in methods
# animals[0] = "dog" # This is not allowed in set as they are unordered and immutable

# To iterate through the loop
# for animal in animals:
#     print(animal, end = " ")
# animals.add("cat")
# animals.clear()
# print(animals.__sizeof__())
# print(animals)



# Tuple = () -> they are unordered and immutable any type of data can be stored and duplicates are allowed

brands = ("toyota", "mercedes", "bmw", "hyundai", "toyota")
# brands[0] = "mahindra" # This is not allowed in tuple as they are immutable
# print(brands.__sizeof__())
# print(help(brands))
# print(len(brands))
# print(brands.index("bmw"));
# print(brands.count("toyota")) # Allows to have duplicates

