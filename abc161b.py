n, m = map(int,input().split())
a = list(map(int,input().split()))

t = sum(a)
a.sort(reverse=True)
for i in range(m):
    if a[i] < t * 1/(4*m):
        print("No")
        exit()

print("Yes")