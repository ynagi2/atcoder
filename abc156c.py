n = int(input())
a = list(map(int,input().split()))

m = sum(a) / len(a)
m = round(m)

cost = 0

for elem in a:
    cost += (elem - m) ** 2

print(cost)