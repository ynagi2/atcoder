n, k, q = map(int,input().split())
a = [int(input()) for _ in range(q)]

points = [k]*n
for i in range(q):
    points[a[i]-1] += 1

for i in range(n):
    if points[i] < q+1:
        print("No")
    else:
        print("Yes")