n, k = map(int,input().split())

d = []
a = []

for i in range(k):
    temp = int(input())
    d.append(temp)

    t = list(map(int,input().split()))
    a.append(t)


a_set = set()
for i in a:
    for j in i:
        a_set.add(j)

print(n - len(a_set))