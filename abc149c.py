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

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            return False

    return True


def main():
    x = i_input()
    i = 0
    while True:
        if is_prime(x+i):
            print(x+i)
            exit()
        else:
            i += 1



if __name__ == '__main__':
    main()