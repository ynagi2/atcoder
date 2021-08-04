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

def main():
    n, m = map_int()
    a = lmap_int()
    b = lmap_int()
    a.sort()
    b.sort()
    i = 0
    j = 0
    ans = 10**9
    while True:
        ans = min(ans, abs(a[i] - b[j]))
        if a[i] > b[j]:
            if j == m - 1:
                break
            j += 1
        elif a[i] < b[j]:
            if i == n - 1:
                break
            i += 1
        else:
            print(0)
            exit()
    print(ans)





if __name__ == '__main__':
    main()