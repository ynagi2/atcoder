# 解説: https://drken1215.hatenablog.com/entry/2020/05/02/225600
# O(N)でも間に合わない
import math
abn = list(map(int,input().split()))

# temp = 0

# for x in range(abn[2] + 1):
#     m = math.floor(abn[0] * x / abn[1]) - abn[0] * math.floor(x / abn[1])

#     if m > temp:
#         temp = m

# print(int(temp))

x = min(abn[1] - 1, abn[2])
m = math.floor(abn[0] * x / abn[1]) - abn[0] * math.floor(x / abn[1])
print(m)