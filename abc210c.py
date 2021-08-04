from collections import defaultdict, deque
from itertools import permutations, combinations
from math import factorial, ceil, floor
from decimal import Decimal

def i_input(): return int(input())
def map_str(): return input().split()
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))
# mod = 10**9 + 7

def main():
    n, k = map_int()
    c = lmap_int()
    d = {}
    for i in range(k):
        if c[i] not in d:
            d[c[i]] = 1
        else:
            d[c[i]] += 1
    ans = len(d)
    for i in range(n-k):
        if c[k+i] not in d:
            d[c[k+i]] = 1
        else:
            d[c[k+i]] += 1
        d[c[i]] -= 1
        if d[c[i]] == 0:
            del d[c[i]]
        ans = max(ans, len(d))
    print(ans)


if __name__ == '__main__':
    main()