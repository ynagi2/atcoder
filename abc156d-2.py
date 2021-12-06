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


# bを法とするaの逆元を返す
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


# 組み合わせはO(n)の計算量だが，以下のようにO(k)にすることもできる
# cf. https://drken1215.hatenablog.com/entry/2018/06/08/210000
def calc_cmb(n, k, mod):
    ans = 1
    for i in range(k):
        ans =  ans * (n - i) % mod
    for i in range(k):
        ans %= mod
        ans = ans * modinv(i+1, mod) % mod
    return ans


def main():
    mod = 10**9 + 7
    n, a, b = map_int()
    ans = pow(2, n, mod) - 1
    ans =  (ans - calc_cmb(n, a, mod)) % mod
    ans = (ans - calc_cmb(n, b, mod)) % mod
    print(ans)


if __name__ == '__main__':
    main()