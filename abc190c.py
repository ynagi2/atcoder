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
    n, m = map_int()
    a, b, c, d = [], [], [], []
    for _ in range(m):
        x, y = map_int()
        a.append(x)
        b.append(y)
    k = i_input()
    for _ in range(k):
        x, y = map_int()
        c.append(x)
        d.append(y)
    
    ans = 0
    for i in range(2**k-1):
        dish = [0]*n
        string = str(bin(2**k-(i+1))[2:])
        if len(string) < k:
            string = '0'*(k - len(string)) + string
        tf = []
        for z in range(k):
            tf.append(int(string[z]))
        for j in range(k):
            if tf[j] == 1:
                dish[d[j]-1] += 1
            else:
                dish[c[j]-1] += 1
        cnt = 0
        for j in range(m):
            if dish[a[j]-1] > 0 and dish[b[j]-1] > 0:
                cnt += 1
            ans = max(ans, cnt)
    print(ans)


if __name__ == '__main__':
    main()