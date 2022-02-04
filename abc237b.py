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
    h, w = map_int()
    a = []
    for i in range(h):
        tmp = lmap_int()
        a.append(tmp)
    for i in range(w):
        tmp = []
        for j in range(h):
            tmp.append(a[j][i])
        print(*tmp)


if __name__ == '__main__':
    main()