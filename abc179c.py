from collections import defaultdict, deque
from itertools import permutations, combinations
from math import factorial, ceil, floor
from decimal import Decimal

def i_input(): return int(input())
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))
# mod = 10**9 + 7

# BとCが1:1対応になる
# 普通に約数列挙しようとするとNlogNで間に合わない
def main():
    n = i_input()
    cnt = 0
    for i in range(1, n):
        if n % i == 0:
            cnt += n // i - 1
        else:
            cnt += n // i
    print(cnt)


if __name__ == '__main__':
    main()