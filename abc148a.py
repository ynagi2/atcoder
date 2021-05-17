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
    a = i_input()
    b = i_input()
    z = set()
    z.add(1)
    z.add(2)
    z.add(3)
    z.remove(a)
    z.remove(b)
    print(z.pop())


if __name__ == '__main__':
    main()