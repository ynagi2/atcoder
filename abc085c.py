import sys
c = list(map(int,input().split()))

for i in range(int(c[0])+1):
    for j in range(int(c[0]) - i + 1):
        if (10000*j + 5000*(int(c[0]) - i - j) + 1000*i) == int(c[1]):
            print("{} {} {}".format(j, int(c[0]) - i - j, i))
            sys.exit()

print("-1 -1 -1")
