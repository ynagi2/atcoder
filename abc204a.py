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
    t = set()
    t.add(0)
    t.add(1)
    t.add(2)
    x, y = map_int()
    if x == y:
        print(x)
    else:
        t.remove(x)
        t.remove(y)
        ans = list(t)
        print(ans[0])


if __name__ == '__main__':
    main()