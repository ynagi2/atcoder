r, d, x = map(int,input().split())

n = x
for i in range(10):
    n = r*n - d
    print(n)