# 2 - Generate pattern with nested loops:
# 1 1 1
#  2 2
# 3 3 3
#  4 4
# 5 5 5

n = 1
while(n <= 5):
    if (n % 2 == 0):
        print('', n, n, '')
        n = n + 1
    else:
        print(n, n, n)
        n = n + 1
