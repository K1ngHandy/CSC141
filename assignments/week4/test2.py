## 1 - What would be displayed as the result of executing the following code?
x = -1
y = 0

x = x + 1
y = x + y
print(y)
# Answer: 0

## 2 - What would be displayed as the result of executing the following code?
x = 10
y = 12

if (x % 2 == 0) and (y % 5 == 0):
    print(y)
else:
    print(x)
# Answer: 10

## 3 - What would be displayed as the result of executing the following code?
x = 10
y = 12

if (x % 2 != 0):
    print(y)
elif (x > 15):
    print(x)
else:
    print("****")
# Answer: ****

## 4 - What would be displayed as the result of executing the following code?
x = 1234.55
print(f'{x:^10.1f}', 5)
# Answer: '  1234.5   5'

## 5 - What would be displayed as the result of executing the following code?
name = "MNPQ"
if (name[1] == "N"):
    temp1 = name[2]
    temp2 = name[3]
    temp3 = name[1]
else:
    temp1 = name[1]
    temp2 = name[3]
    temp3 = name[2]

print(temp3 + temp1)
# Answer: NP
