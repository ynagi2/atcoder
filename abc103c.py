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

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def main():
    n = i_input()
    a = lmap_int()
    for i in range(n-1):
        if i == 0:
            m = a[i] * a[i+1] // gcd(a[i], a[i+1])
        else:
            m = m * a[i+1] // gcd(m, a[i+1])
    m -= 1
    ans = 0
    for e in a:
        ans += m % e
    print(ans)


if __name__ == '__main__':
    main()