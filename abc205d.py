from collections import defaultdict, deque
from itertools import permutations, combinations
from math import factorial, ceil, floor
from decimal import Decimal
from bisect import bisect_right, bisect_left

def i_input(): return int(input())
def map_str(): return input().split()
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))
# mod = 10**9 + 7

def main():
    n, q = map_int()
    a = lmap_int()
    c = [0]*n
    for i, e in enumerate(a):
        c[i] = e - i - 1
    for _ in range(q):
        k = i_input()
        # kを挿入できる最も左側を得る
        idx = bisect_left(c, k)
        if idx == 0:
            print(k)
        else:
            # aに含まれている分だけ追加で足す
            print(k + idx)


if __name__ == '__main__':
    main()