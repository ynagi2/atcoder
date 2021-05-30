from collections import defaultdict, deque
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
    s = input()
    yes = set()
    no = set()
    other = set()
    for i, e in enumerate(s):
        if e == "o":
            yes.add(str(i))
        elif e == "x":
            no.add(str(i))
        else:
            other.add(str(i))
    ans = 0
    for i in range(10000):
        num = "{:04d}".format(i)
        cnt = set()
        f = True
        for e in num:
            if e in no:
                f = False
            if e in yes:
                cnt.add(e)
        if f and cnt == yes:
            ans += 1
    print(ans)



if __name__ == '__main__':
    main()