import sys
n = int(input())
a = list(map(int,input().split()))

s = 0
while 0 not in a:
    for i,elem in enumerate(a):
        if elem % 2 != 0:
            print(s)
            sys.exit()
        else:
            a[i] /= 2

    s += 1

print(s)