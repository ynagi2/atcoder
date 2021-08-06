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

import heapq

def main():
    q = i_input()
    m = []
    cost = 0
    heapq.heapify(m)
    for i in range(q):
        tmp = input()
        p = int(tmp[0])
        if p != 3:
            x = int(tmp[2:])
        
        if p == 1:
            heapq.heappush(m, x - cost)
        elif p == 2:
            cost += x
        else:
            print(heapq.heappop(m) + cost)



if __name__ == '__main__':
    main()