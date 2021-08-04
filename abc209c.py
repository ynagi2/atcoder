from collections import defaultdict, deque
from itertools import permutations, combinations
from math import factorial, ceil, floor
from decimal import Decimal

def i_input(): return int(input())
def map_str(): return input().split()
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

def main():
    n = i_input()
    c = lmap_int()
    mod = 10**9 + 7
    c.sort()
    ans = 1
    for i in range(n):
        ans = (c[i] - i) * ans % mod
    print(ans)



if __name__ == '__main__':
    main()