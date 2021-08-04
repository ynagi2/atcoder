from collections import defaultdict, deque
from itertools import permutations, combinations
from math import factorial, ceil, floor
from decimal import Decimal

def i_input(): return int(input())
def map_str(): return input().split()
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

def main():
    mod = 10**9 + 7
    s = input()
    n = len(s)
    t = "chokudai"
    dp = [[0 for _ in range(len(t)+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(n):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i+1][j+1] = (dp[i][j+1] + dp[i][j]) % mod
            else:
                dp[i+1][j+1] = dp[i][j+1]
    print(dp[n][len(t)])


if __name__ == '__main__':
    main()