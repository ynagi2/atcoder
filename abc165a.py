k = int(input())
ab = list(map(int,input().split()))

f = False
i = ab[0]
while i <= ab[1]:
    if i % k == 0:
        print("OK")
        f = True
        break
    i += 1

if f is False:
    print("NG")

