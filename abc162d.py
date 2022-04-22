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
    s = input()
    ss = defaultdict(int)
    for e in s:
        ss[e] += 1
    val = ss["R"] * ss["G"] * ss["B"]
    if val == 0:
        print(0)
        exit()
    cnt = 0
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            k = 2*j - i
            if j < k and k < n and s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                cnt += 1
    print(val - cnt)


if __name__ == '__main__':
    main()