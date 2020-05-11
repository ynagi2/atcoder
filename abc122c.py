n, q = map(int,input().split())
s = input()
l = []
r = []
for _ in range(q):
    a, b = map(int,input().split())
    l.append(a)
    r.append(b)

acsum = [0]*(n+1)
for i in range(len(s) - 1):
    if s[i:i+2] == "AC":
        acsum[i+2] = acsum[i+1] + 1
    else:
        acsum[i+2] = acsum[i+1]

for le, re in zip(l, r):
    print(acsum[re] - acsum[le])