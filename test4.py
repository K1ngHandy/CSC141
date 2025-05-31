number=int(input("Enter a number:"))
print(number**2, number**3)
print(number*number, "\t", number**2) # tab inserted

## Area of a triangle A=(side*h/2)
Side=float(input("What is length of a side? "))
HG=float(input("What is the height? "))
AreaTriangle=Side*HG/2
print("Triangle area is", AreaTriangle)
print("Triangle area is", Side*HG/2)

## Area of a circle A=Pi*R*R
R=float(input("Enter radius: "))
AreaCircle=3.14*R*R
print("Circle Area is:", AreaCircle)

## Get name and display 4 times
name=input("What is your name? ")
print(name*3)
