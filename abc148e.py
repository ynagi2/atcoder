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

# 単に5**1, 5**2, ...でそれぞれ割り切れる個数をカウントすればよい
def main():
    n = i_input()
    a = 10
    ans = 0
    if n % 2 == 1:
        print(0)
    else:
        while a <= n:
            ans += n//a
            a *= 5
        print(ans)

if __name__ == '__main__':
    main()