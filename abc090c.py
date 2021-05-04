from collections import defaultdict
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
    n, m = map_int()
    if n == 1 and m == 1:
        print(1)
    elif n == 1:
        print(m-2)
    elif m == 1:
        print(n-2)
    else:
        print((n-2)*(m-2))


if __name__ == '__main__':
    main()