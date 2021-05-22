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
    a = lmap_int()
    b = lmap_int()
    c = lmap_int()
    score = defaultdict(int)
    for i in range(n):
        score[b[c[i]-1]] += 1
    ans = 0
    for i in range(n):
        ans += score[a[i]]
    print(ans)



if __name__ == '__main__':
    main()