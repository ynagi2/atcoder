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
    n, k = map_int()
    ab = []
    for _ in range(n):
        x, y = map_int()
        ab.append([x, y])
    ab.sort()
    ans = k
    for i in range(n):
        if ab[i][0] <= ans:
            ans += ab[i][1]
    print(min(10**100, ans))



if __name__ == '__main__':
    main()