## 1 Single num n to display pattern n, nn, nnn
n=int(input("Enter a number"))
print("Number pattern:", n, n*11, n*111)

## 2 Generate flag pattern
stars='* '
stripes='='
print(stars * 6 + stripes * 35)
print(' ' + stars * 5 + ' ' + stripes * 35)
print(stars * 6 + stripes * 35)
print(' ' + stars * 5 + ' ' + stripes * 35)
print(stars * 6 + stripes * 35)
print(' ' + stars * 5 + ' ' + stripes * 35)
print(stars * 6 + stripes * 35)
print(' ' + stars * 5 + ' ' + stripes * 35)
print(stars * 6 + stripes * 35)
print(stripes * 47)
print(stripes * 47)
print(stripes * 47)
print(stripes * 47)
print(stripes * 47)
print(stripes * 47)

## 3 Receive odd number input then display 2 previous and next 2 numbers
oddInput = int(input("Enter odd number: "))
odd = oddInput % 2 == 1

if odd:
    # previous 2 odd numbers
    prev1 = oddInput - 2
    prev2 = oddInput - 4

    # next 2 odd numbers
    next1 = oddInput + 2
    next2 = oddInput + 4

    print(prev2, prev1, oddInput, next1, next2)
else:
    print("Enter an odd number.")

## 4 Receive triangle base and height inputs then calculate area
base = int(input("Base of triangle: "))
height = int(input("Height of triangle: "))
area = (base * height) / 2
print("Area of triangle:", area)
