n = int(input())

a = list(map(int, input().split()))

count_positive = 0

for x in a:
    if x > 0:
        count_positive += 1

print(count_positive)