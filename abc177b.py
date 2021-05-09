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

# sのどこをtの1文字目(スタート)にするかを決め，そこからのdiffをカウント
def main():
    s = input()
    t = input()

    ans = len(t)
    for i in range(len(s)-len(t)+1):
        cnt = 0
        for j in range(len(t)):
            if t[j] != s[i+j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()