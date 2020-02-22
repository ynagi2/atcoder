a = list(map(int,input().split()))

if a[0] < 10:
    print(a[1] + 100*(10-a[0]))
else:
    print(a[1])
