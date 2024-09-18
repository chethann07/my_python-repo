# Some of the string methods
# To know about all the string 

s = "Hello World"
s2 = "hello world"
phonenum = "91-9999999999"

length = len(s)
find1 = s.find("o")
find2 = s.rfind("o")
s2 = s2.capitalize()
s2 = s2.upper()
s2 = s2.lower()
isDigit = s2.isdigit()
isAlpha = s2.isalpha()
count = s.count("o")
replace = phonenum.replace("91-","")

print(replace)