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
def modinv(a, b):
    p = b
    x, y, u, v = 1, 0, 0, 1
    while b:
        k = a // b
        x -= k * u
        y -= k * v
        x, u = u, x
        y, v = v, y
        a, b = b, a % b
    x %= p
    if x < 0:
        x += p
    return x


def main():
    mod = 998244353
    n = iipt()
    str_n = str(n)
    str_n = str_n[::-1]
    ans = 0
    for i in range(len(str_n)-1):
        tmp = 9 * pow(10, i, mod)
        value = tmp * (tmp + 1) % mod
        value = value * modinv(2, mod)
        ans = ans + value % mod
    val = n - 10**(len(str_n) - 1) + 1
    x = val * (val + 1) % mod
    x = x * modinv(2, mod)
    ans = ans + x % mod
    print(ans % mod)


if __name__ == '__main__':
    main()