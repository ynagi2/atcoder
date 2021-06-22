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

# ^: xor &: and |: or
def main():
    n = i_input()
    a = lmap_int()
    ans = 2**30
    for i in range(2**(n-1)):
        x, y = a[0], 0
        string = "{:020b}".format(i)
        string = string[20-(n-1):]
        string = string[::-1]
        for j in range(n-1):
            if string[j] == "1":
                y = y ^ x
                x = a[j+1]
            else:
                x = x | a[j+1]
        y = y ^ x
        ans = min(ans, y)
    print(ans)





if __name__ == '__main__':
    main()