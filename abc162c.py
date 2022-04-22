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

import sys
sys.setrecursionlimit(3 * 10 ** 5)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


def main():
    k = iipt()
    ans = 0
    for a in range(1, k+1):
        for b in range(1, k+1):
            for c in range(1, k+1):
                val = gcd(a, b)
                val = gcd(val, c)
                ans += val
    print(ans)


if __name__ == '__main__':
    main()