n = int(input())
s = input()

w = [0]*(n+1)
e = [0]*(n+1)

# e,wの累積和を記録
for i, d in enumerate(s):
    if d == "W":
        w[i+1] = w[i] + 1
        e[i+1] = e[i]
    else:
        e[i+1] = e[i] + 1
        w[i+1] = w[i]

mnum = n
for i, d in enumerate(s):
    mnum = min(mnum, w[i] + e[n] - e[i+1])

print(mnum)