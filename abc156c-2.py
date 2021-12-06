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
    x = lmap_int()
    ans = 10**19
    for i in range(100):
        cost = 0
        for e in x:
            cost += (e - (i+1))**2
        ans = min(ans, cost)
    print(ans)


if __name__ == '__main__':
    main()