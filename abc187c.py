from itertools import permutations
from math import factorial, ceil, floor

def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))
# mod = 10**9 + 7

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    t = set()
    for e in s:
        t.add(e)
        if e[0] == "!":
            if e[1:] in t and e in t:
                print(e[1:])
                exit()
        else:
            if e in t and "!"+e in t:
                print(e)
                exit()
    print("satisfiable")



if __name__ == '__main__':
    main()