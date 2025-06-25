# 1 - Prime number checker
num = int(input("Enter a number to check if prime: "))
prime = True # assume true until checked

# 1 is not prime
if num <= 1:
    prime = False

# Check if divisible by 1 and itself
if (num % 1 == 0):
    print(f"{num} is divisible by 1,")
    if (num % num == 0):
        print("...divisible by itself,")

# Check if divisible by a number from 2 to num - 1
for i in range(2, num):
    if (num % i == 0):
        prime = False # if divisible by any other number
        divisor = i
        break # exit loop early

# Output result
if prime:
    print("...and not divisible by another number.")
    print(f"{num} is a Prime number!")
elif not prime:
    if divisor: # if divisor is found in loop
        print(f"...and divisible by {divisor}.")
    print(f"{num} is NOT a Prime number!")
