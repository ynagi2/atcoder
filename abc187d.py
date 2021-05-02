from itertools import permutations
from math import factorial, ceil, floor

def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))
# mod = 10**9 + 7

def main():
    n = int(input())
    ab = []
    aoki = 0
    for _ in range(n):
        x, y = map_int()
        ab.append([2*x+y, x, y])
        aoki += x
    ab.sort(reverse=True)
    taka = 0
    ans = 0
    for i in range(n):
        aoki -= ab[i][1]
        taka += ab[i][1] + ab[i][2]
        ans += 1
        if taka > aoki:
            break
    print(ans)



if __name__ == '__main__':
    main()