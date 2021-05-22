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

def combinations_count(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))

def main():
    a, b, k = lmap_int()
    l = ["a"]*a + ["b"]*b
    n = a + b
    cnt1 = 1
    cnt2 = 1
    ad = 0
    ans = ""
    rest = 0
    for i in range(n):
        if a-cnt2 < 0:
            rest = n-cnt1+1
            break
        compare = combinations_count(n-cnt1, a-cnt2)
        if k <= compare + ad:
            cnt1 += 1
            cnt2 += 1
            ans += "a"
        else:
            cnt1 += 1
            ans += "b"
            ad += compare
    for i in range(rest):
        ans += "b"
    print(ans)




if __name__ == '__main__':
    main()