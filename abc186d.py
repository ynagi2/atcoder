from itertools import permutations
from math import factorial, ceil, floor

def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))
# mod = 10**9 + 7

def main():
    n = int(input())
    a = lmap_int()
    a.sort(reverse=True)
    ans = 0
    for i, e in enumerate(a):
        ans += (n-1-i)*e
        ans -= i*e
    print(ans)


if __name__ == '__main__':
    main()