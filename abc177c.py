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

def main():
    mod = 10**9 + 7
    n = i_input()
    a = lmap_int()

    asum = [0]*(n+1)
    for i in range(n):
        asum[i+1] = asum[i] + a[i]
    
    ans = 0
    for i in range(n):
        ans += a[i] * (asum[n] - asum[i+1]) % mod
    print(ans % mod)



if __name__ == '__main__':
    main()