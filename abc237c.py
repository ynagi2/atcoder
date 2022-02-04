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
    cnt = 0
    for i in range(len(s)):
        if s[i] == s[-(i+1)] and s[i] == "a":
            cnt += 1
        else:
            break
    if cnt > 0: s = s[cnt:-cnt]
    new_s = s[::-1]
    j = ""
    for i in range(len(new_s)):
        if new_s[i] != "a":
            j = new_s[i:]
            break
    ans = "Yes"
    for i in range(len(j)):
        if j[i] != j[-(i+1)]:
            ans = "No"
    print(ans)

if __name__ == '__main__':
    main()