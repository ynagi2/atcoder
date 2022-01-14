from collections import defaultdict, deque
from itertools import permutations, combinations
from math import factorial, ceil, floor
from decimal import Decimal
import heapq

def iipt(): return int(input())
def map_str(): return input().split()
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))
# mod = 10**9 + 7

def main():
    a, b = map_int()
    price = 1009
    ans = -1
    while price > 0:
        if floor(price*0.08) == a and floor(price*0.10) == b:
            ans = price
        price -= 1
    print(ans)


if __name__ == '__main__':
    main()