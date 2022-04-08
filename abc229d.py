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
    s = input()
    k = iipt()
    ans = 0
    dotsum = [0]*(len(s)+1)
    for i in range(len(s)):
        dotsum[i+1] = dotsum[i]
        if s[i] == ".": dotsum[i+1] += 1
    right = 0
    for left in range(len(s)):
        # 累積和で判定するという発想
        while right <= len(s) - 1 and (dotsum[right+1] - dotsum[left] <= k):
            right += 1
        ans = max(ans, right - left)
    print(ans)


if __name__ == '__main__':
    main()