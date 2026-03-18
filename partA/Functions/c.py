def xor(x, y):
    if x != y:
        return 1
    else:
        return 0

line = input().split()
x = int(line[0])
y = int(line[1])

print(xor(x, y))