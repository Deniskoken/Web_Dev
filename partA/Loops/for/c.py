import math

a = int(input())
b = int(input())

for x in range(a, b + 1):
    tbir = math.sqrt(x)
    if int(tbir) ** 2 == x:
        print(x, end=" ")