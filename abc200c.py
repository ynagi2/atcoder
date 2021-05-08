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
    val = []
    for e in a:
        val.append(e % 200)
    dic = {}
    cnt = 0
    for e in val:
        if e not in dic.keys():
            dic[e] = 1
        else:
            cnt += dic[e]
            dic[e] += 1
    print(cnt)



if __name__ == '__main__':
    main()