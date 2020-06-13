import math
x, y = map(int,input().split())

# 1x, 2x, 4x, ... の個数を数える
l = 0
while x <= y:
    l += 1
    x = 2*x

print(l)

# なぜWA?
# print(int(math.log2(int(y/x)) + 1))