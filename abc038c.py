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
    n = iipt()
    a = lmap_int()
    ans = 0
    right = 1
    for left in range(n):
        # whileの条件を満たさないとright++されない(rightは開区間のイメージ)
        # right <= left がないとright == left のまま足される
        while right < n and (right <= left or a[right-1] < a[right]):
            right += 1
        ans += right - left
    print(ans)


if __name__ == '__main__':
    main()