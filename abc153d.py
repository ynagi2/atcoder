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
    h = iipt()
    i = 1
    while True:
        if h < 2 ** i:
            print(2 ** i - 1)
            exit()
        else:
            i += 1





if __name__ == '__main__':
    main()