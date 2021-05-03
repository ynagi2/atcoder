from collections import defaultdict
from itertools import permutations, combinations
from math import factorial, ceil, floor
from decimal import Decimal

def i_input(): return int(input())
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))
# mod = 10**9 + 7

# s,t,pでの流量を辞書で持っておくことで，同じstart値が複数合ってもまとめて処理できる
# imos法のアイデアで，startとendの流量に注目して増減させればよい
def main():
    n, w = map_int()
    sp = defaultdict(int)
    tp = defaultdict(int)
    for _ in range(n):
        x, y, z = map_int()
        sp[x] += z
        tp[y] += z
    
    cnt = 0
    for i in range(2+10**5+1):
        cnt += sp[i]
        cnt -= tp[i]
        if cnt > w:
            print("No")
            exit()
    print("Yes")


if __name__ == '__main__':
    main()