# 配列での二分探索で便利
# どのエントリーよりも後ろ(右)にくるような挿入点を返す
# import bisect_right とすればより明示的(bisect_leftもある)
from bisect import bisect

n, k = map(int,input().split())
a = list(map(int,input().split()))

# 部分文字列を端を固定して求めようとすると，O(N^2)になる
asum = [0]*(n+1)
for i in range(n):
    asum[i+1] = asum[i] + a[i]

# 各左端について，累積和の二分探索で何個の右端が条件を満たすかカウント
count = 0
for e in asum:
    # eがk未満なら勿論0(そのeを右端にしても条件に合うものはない)
    # e - k がasumのどこに位置するか探し，e - k の位置よりも左にある要素の数を足していく
      # そのeを右端にして，どこまで要素を削れるか探す
    count += bisect(asum, e - k)

print(count)