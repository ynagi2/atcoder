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
    n, k = map_int()
    s = []
    is_in_zero = False
    for _ in range(n):
        val = iipt()
        if val == 0: is_in_zero = True
        s.append(val)
    if is_in_zero:
        print(n)
        exit()
    ans = 0
    right = 0
    pprod = 1
    for left in range(n):
        # whileの条件を満たさないとright++されない(rightは開区間のイメージ)
        while right < n and pprod * s[right] <= k:
            pprod *= s[right]
            right += 1
        ans = max(ans, right - left)
        # leftのインデックスから積を計算していくので
        if right == left:
            right += 1
        else:
            pprod /= s[left]
    print(ans)


if __name__ == '__main__':
    main()