from collections import defaultdict, deque
from itertools import permutations, combinations
from math import factorial, ceil, floor
from decimal import Decimal
import heapq

def iipt(): return int(input())
def map_str(): return input().split()
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))
# mod = 10**9 + 7

# 頭悪いので愚直にシミュレーションしてTLE
# 切れ込み最大でも360しかないので全箇所記録して引き算でおk
def main():
    n = iipt()
    a = lmap_int()
    cut = []
    s = 0
    for e in a:
        s += e
        cut.append(s % 360)
    cut.sort()
    ans = cut[0]
    for i in range(len(cut)-1):
        comp = cut[i+1] - cut[i]
        ans = max(ans, comp)
    ans = max(ans, 360 - cut[-1])
    print(ans)

if __name__ == '__main__':
    main()