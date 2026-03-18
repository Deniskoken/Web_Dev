def min4(a, b, c, d):
    m1 = a
    if b < m1:
        m1 = b
        m2 = c
    if d < m2:
        m2 = d
    
    if m1 < m2:
        return m1
    else:
        return m2

nums = list(map(int, input().split()))

print(min4(nums[0], nums[1], nums[2], nums[3]))