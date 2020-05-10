a, b, c, k = map(int,input().split())

value = 0
if a >= k:
    value = k
    print(value)
else:
    value = a
    if k <= a + b:
        print(value)
    else:
        value += (k-a-b) * (-1)
        print(value)

