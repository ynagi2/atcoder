n = int(input())
a = list(map(int,input().split()))

sa = set(a)

if len(a) == len(sa):
    print("YES")
else:
    print("NO")

