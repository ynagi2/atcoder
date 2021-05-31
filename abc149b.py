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
    a, b, k = map_int()
    ans_a = max(a-k, 0)
    if ans_a > 0:
        ans_b = b
    else:
        ans_b = max(b-(k-a), 0)
    print("{} {}".format(ans_a, ans_b))


if __name__ == '__main__':
    main()