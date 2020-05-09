n = int(input())
a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))

# 累積和を使ってみる
s1 = [0]*(n+1)
for i in range(n):
    s1[i+1] = s1[i] + a1[i]

s2 = [0]*(n+1)
for i in range(n):
    s2[i+1] = s2[i] + a2[i]

cmax = 0
for i in range(n):
    cmax = max(cmax, s1[i+1] + s2[n] - s2[i])

print(cmax)