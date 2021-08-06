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
    n, m = map_int()
    tmp = lmap_int()
    a = [e*(-1) for e in tmp]
    heapq.heapify(a)
    for _ in range(m):
        val = heapq.heappop(a) * (-1)
        val = val // 2
        heapq.heappush(a, -val)
    print(-sum(a))



if __name__ == '__main__':
    main()