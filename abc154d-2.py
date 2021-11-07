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
    n, k = map_int()
    p = lmap_int()
    pos = 0
    idx = 0
    psum = [0]*(n+1)
    for i in range(n):
        psum[i+1] = psum[i] + p[i]
    for i in range(n-k+1):
        s = psum[i+k] - psum[i]
        if pos < s:
            pos = s
            idx = i
    ans = 0
    for i in range(k):
        ans += (p[i+idx] + 1) / 2
    print(ans)



if __name__ == '__main__':
    main()