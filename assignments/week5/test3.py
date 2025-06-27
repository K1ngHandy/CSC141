# Steve Handy
# CSC 141

# 1
for i in range(2):
    for j in range(1):
        print(i + j)

# 2
for i in range(0, 6):
    print(i * (5 - i))
    print("\n")

# 3
for i in range(1, 4):
    print("For ", i, " the cube is : ", (i * i * i))

# 4
a = -123.56
print(f'{a:8.2f}')

# 5
a = 15
a = a - 1
b = 10
a = b
if(a % 2 != 0) and (b % 2 == 0):
    print("******")
else:
    print(".....")

# 6
name = "ABCDE"
for i in range(0, len(name)):
    print(name[i - 1])

# 7
name = "ABCDEF"
for i in range(0, len(name) // 3):
    for j in range(len(name) // 3):
        print(name[(i + j) // 2])
