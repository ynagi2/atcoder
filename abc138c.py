n = int(input())
v = list(map(int,input().split()))

v.sort()

while len(v) > 2:
    v.append((v[0] + v[1]) / 2)
    v.remove(v[0])
    v.remove(v[0])
    v.sort()

print((v[0] + v[1]) / 2)