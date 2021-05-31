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

# 貪欲法で最適解が得られるとは思わなかった
# DPで解く場合は，mod kでk個のグループに分割し，各グループについてDPすればよい
def main():
    n, k = map_int()
    r, s, p = map_int()
    t = input()

    his = ""
    ans = 0
    for i in range(n):
        if i < k:
            if t[i] == "r":
                his += "p"
                ans += p
            elif t[i] == "s":
                his += "r"
                ans += r
            else:
                his += "s"
                ans += s
        else:
            if t[i] == "r":
                if his[i-k] == "p":
                    his += "*"
                else:
                    his += "p"
                    ans += p
            elif t[i] == "s":
                if his[i-k] == "r":
                    his += "*"
                else:
                    his += "r"
                    ans += r
            else:
                if his[i-k] == "s":
                    his += "*"
                else:
                    his += "s"
                    ans += s
    print(ans)


if __name__ == '__main__':
    main()