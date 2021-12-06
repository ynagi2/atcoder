# 早くなるおまじない
# 文字列読み込みの際には注意
# import sys
# input = sys.stdin.buffer.readline

# 再帰関数の呼び出し制限
# sys.setrecursionlimit(3 * 10 ** 5)
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
    n, r = map_int()
    if n >= 10:
        print(r)
    else:
        print(r + 100 * (10 - n))


if __name__ == '__main__':
    main()