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
    h, w, n = map_int()
    ab = []
    for i in range(n):
        x, y = map_int()
        ab.append([x, y, i+1])
    ab.sort(key=lambda x: x[0])
    for i in range(n):
        if i == 0:
            val = 1
            prev = ab[i][0]
            ab[i][0] = val
        else:
            if prev == ab[i][0]:
                ab[i][0] = val
            else:
                val += 1
                prev = ab[i][0]
                ab[i][0] = val
    
    ab.sort(key=lambda x: x[1])
    for i in range(n):
        if i == 0:
            val = 1
            prev = ab[i][1]
            ab[i][1] = val
        else:
            if prev == ab[i][1]:
                ab[i][1] = val
            else:
                val += 1
                prev = ab[i][1]
                ab[i][1] = val
    
    ab.sort(key=lambda x: x[2])

    for i in range(n):
        print("{} {}".format(ab[i][0], ab[i][1]))




if __name__ == '__main__':
    main()