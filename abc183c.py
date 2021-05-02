from itertools import permutations
import math

def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))
# mod = 10**9 + 7

def main():
    n, k = map_int()
    t = []
    for i in range(n):
        t.append(lmap_int())
    pat = [i+1 for i in range(n-1)]
    ans = 0
    for p in permutations(pat, n-1):
        tim = 0
        for j, e in enumerate(p):
            if j == 0:
                tim += t[j][e]
            else:
                tim += t[preb][e]
            preb = e
        tim += t[preb][0]
        if tim == k: ans += 1
    print(ans)


if __name__ == '__main__':
    main()