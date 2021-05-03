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

def main():
    n = i_input()
    a = lmap_int()
    costs = []
    for i in range(n+1):
        if i == 0:
            costs.append(abs(a[i]))
        elif i == n:
            costs.append(abs(a[i-1]))
        else:
            costs.append(abs(a[i]-a[i-1]))
    sum_cost = sum(costs)
    for i in range(n):
        if i == 0:
            print(sum_cost - costs[i] - costs[i+1] + abs(a[i+1]))
        elif i == n-1:
            print(sum_cost - costs[i] - costs[i+1] + abs(a[i-1]))
        else:
            print(sum_cost - costs[i] - costs[i+1] + abs(a[i+1] - a[i-1]))


if __name__ == '__main__':
    main()