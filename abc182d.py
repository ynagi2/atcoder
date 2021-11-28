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

def main():
    n = iipt()
    a = lmap_int()
    asum = [0]*(n+1)
    for i in range(n):
        asum[i+1] = asum[i] + a[i]
    amax = [0]*(n+1)
    for i in range(n):
        amax[i+1] = max(amax[i], asum[i+1])
    ans = 0
    pos = 0
    for i in range(n):
        ans = max(ans, pos + amax[i+1])
        pos += asum[i+1]
    print(ans)



if __name__ == '__main__':
    main()