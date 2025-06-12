## Stephen Handy
## CSC141
# Homework #2

## 1 - Write a program to get a number between 1-12 and determine the corresponding month
month = int(input("Enter a month number (1-12): "))
if (month < 1 or month > 12):
    print("Invalid month")
else:
    if (month == 1):
        print("January")
    elif(month == 2):
        print("February")
    elif(month == 3):
        print("March")
    elif(month == 4):
        print("April")
    elif(month == 5):
        print("May")
    elif(month == 6):
        print("June")
    elif(month == 7):
        print("July")
    elif(month == 8):
        print("August")
    elif(month == 9):
        print("September")
    elif(month == 10):
        print("October")
    elif(month == 11):
        print("November")
    else:
        print("December")

## 2 - Write a program to get a person’s age and determine the ticket price. 
    # $2 for a child (no more than 10 years), $3 for a senior (at least 65 years), or $5 for an adult.
age = int(input("Enter your age: "))
if (age < 1):
    print("Invalid age")
elif(age <= 10):
    print("Child ticket price: $2")
elif(age >= 65):
    print("Senior ticket price: $3")
else:
    print("Adult ticket price: $5")

## 3 - Write a program to get a date and determine the day of the week.
    # To determine the day of the week, given the month, day, and year, you can use Zeller’s formula.
    # want MM/DD/YYYY as input reques and output day of the week using Zeller's congruence
date = input ("Enter a date (MM/DD/YYYY): ")
m, q, y = map(int, date.split('/'))
# Zeller's Congruence, where m is month, q is day of the month, and y is the year.
h = (q + ((13 * (m + 1)) // 5) + y % 100 + (y % 100) // 4 + (y // 100) // 4 - 2 * (y // 100)) % 7

if (h == 0):
    h = "Saturday"
elif(h == 1):
    h = "Sunday"
elif(h == 2):
    h = "Monday"
elif(h == 3):
    h = "Tuesday"
elif(h == 4):
    h = "Wednesday"
elif(h == 5):
    h = "Thursday"
elif(h == 6):
    h = "Friday"

print("Day of the week is:", h)
