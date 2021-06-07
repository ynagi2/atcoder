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
    t = lmap_int()
    s = sum(t)
    # dp[i][j] i番目までの数を用いたり用いなかったりすることで，jという値は作れるか
    # e.g. d[1]については，8と3を用いることができるので，indexが0,3,8,11のところだけTrueになる
    dp = [[False]*(s+1) for _ in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(s+1):
            if (j - t[i] >= 0 and dp[i][j - t[i]]) or dp[i][j]:
                dp[i+1][j] = True
    ans = 10 ** 6
    for i in range(s+1):
        if dp[n][i]:
            score = max(i, s - i)
            ans = min(ans, score)
    print(ans)

if __name__ == '__main__':
    main()