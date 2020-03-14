import math
a = list(map(int,input().split()))

m = 0
h = a[0]
w = a[1]

'''
#これでも可能？
for hi in range(h):
    for wi in range(w):
        if (hi+1 + wi+1) % 2 == 0:
            m += 1
'''

#行か列が1しかないと角は動けない
if h == 1 or w == 1:
    print(1)
else:
    m = math.ceil(w/2) * math.ceil(h/2) + math.floor(w/2) * math.floor(h/2)
    print(m)

