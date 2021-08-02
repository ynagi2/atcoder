from collections import defaultdict, deque
from itertools import permutations, combinations
from math import factorial, ceil, floor
from decimal import Decimal

def i_input(): return int(input())
def map_str(): return input().split()
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))
# mod = 10**9 + 7

def main():
    n = i_input()
    val = [[0]*9 for _ in range(9)]
    for i in range(n):
        s = str(i+1)
        if s[-1] != "0":
            val[int(s[0])-1][int(s[-1])-1] += 1
    ans = 0
    for i in range(9):
        for j in range(9):
            ans += val[i][j] * val[j][i]
    print(ans)


if __name__ == '__main__':
    main()