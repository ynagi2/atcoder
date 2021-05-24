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
    n, cost = lmap_int()
    d = defaultdict(int)
    for _ in range(n):
        x, y, z = lmap_int()
        d[x] += z
        d[y+1] -= z
    sorted_d = sorted(d)
    for i in range(1, len(sorted_d)):
        d[sorted_d[i]] += d[sorted_d[i-1]]
    for e in d:
        d[e] = min(cost, d[e])

    ans = 0
    for i in range(len(sorted_d) - 1):
        ans += d[sorted_d[i]] * (sorted_d[i+1] - sorted_d[i])
    print(ans)


if __name__ == '__main__':
    main()