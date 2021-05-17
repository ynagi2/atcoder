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
    n = i_input()
    u = input()
    u = u.split()
    s, t = u[0], u[1]
    ans = ""
    for i in range(n):
        ans += s[i] + t[i]
    print(ans)


if __name__ == '__main__':
    main()