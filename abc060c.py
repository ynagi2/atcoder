NT = list(map(int,input().split()))
t = list(map(int,input().split()))

o = 0
for i in range(NT[0] - 1):
    # お湯が一度止まる
    if t[i+1] - t[i] >= NT[1]:
        o += NT[1]
    else:
        o += t[i+1] - t[i]

print(o + NT[1])