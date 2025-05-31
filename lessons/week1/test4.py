# number=int(input("Enter a number:"))
# print(number**2, number**3)
# print(number*number, "\t", number**2) # tab inserted

# ## Area of a triangle A=(side*h/2)
# Side=float(input("What is length of a side? "))
# HG=float(input("What is the height? "))
# AreaTriangle=Side*HG/2
# print("Triangle area is", AreaTriangle)
# print("Triangle area is", Side*HG/2)

# ## Area of a circle A=Pi*R*R
# R=float(input("Enter radius: "))
# AreaCircle=3.14*R*R
# print("Circle Area is:", AreaCircle)

# ## Get name and display 4 times
# name=input("What is your name? ")
# print(name*3)

# ## Concatenation of strings and tuples
# temp1 = "AAA"
# temp2 = "BB"
# print(temp1)
# print(temp2)
# print(temp1 + temp2)  # concatenation of str
# print(temp1, temp2)  # tuple
# print(temp1 + "***" + temp2)  # concatenation with separator
# print(temp1, "***", temp2) # tuple with separator

# # Division operators
# a = 100
# print(a)
# print(a / 2)  # division
# print(a / 2.0)  # division with float
# print(a // 2)  # floor division

# # Mod % -> remainder
# a = 10
# b = 5
# print(a / b)  # division
# print(a // b)  # floor division
# print('Remainder:', a % b)  # remainder of division

# Extracting digits from a number
num = int(input("Enter number: "))
d1 = num // 10
d2 = num % 10

print(d1) # first digit
print(d2) # second digit
