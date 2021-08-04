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

def check(t, l, r, i, j, ans):
    if t[i] == 1 or t[i] == 2:
        min_i = l[i]
    elif t[i] == 3 or t[i] == 4:
        min_i = l[i] + 0.1
    if t[i] == 1 or t[i] == 3:
        max_i = r[i]
    elif t[i] == 2 or t[i] == 4:
        max_i = r[i] - 0.1
        
    if t[j] == 1 or t[j] == 2:
        min_j = l[j]
    elif t[j] == 3 or t[j] == 4:
        min_j = l[j] + 0.1
    if t[j] == 1 or t[j] == 3:
        max_j = r[j]
    elif t[j] == 2 or t[j] == 4:
        max_j = r[j] - 0.1

    if min_j >= min_i and min_j <= max_i:
        ans += 1
    elif max_j >= min_i and max_j <= max_i:
        ans += 1
    elif min_i >= min_j and min_i <= max_j:
        ans += 1
    elif max_i >= min_j and max_i <= max_j:
        ans += 1

    return ans
    


def main():
    n = i_input()
    t, l, r = [], [], []
    for _ in range(n):
        x, y, z = map_int()
        t.append(x)
        l.append(y)
        r.append(z)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans = check(t, l, r, i, j, ans)
    print(ans)


if __name__ == '__main__':
    main()