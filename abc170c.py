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
    x, n = map_int()
    p = lmap_int()
    i = 0
    while True:
        if x-i not in p:
            print(x-i)
            exit()
        elif x+i not in p:
            print(x+i)
            exit()
        else:
            i += 1


if __name__ == '__main__':
    main()