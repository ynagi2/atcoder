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

# 文字列やリストの先頭にinsertを行うのは遅い
# 両端のみにアクセスしたいときはdequeを使うと早い
def main():
    s = deque(input())
    q = i_input()
    f = True
    for _ in range(q):
        tmp = input().split()
        if tmp[0] == '1':
            f = False if f else True
        else:
            if tmp[1] == '1':
                if f:
                    s.appendleft(tmp[2])
                else:
                    s.append(tmp[2])
            else:
                if f:
                    s.append(tmp[2])
                else:
                    s.appendleft(tmp[2])
    if f:
        print(''.join(s))
    else:
        print(''.join(reversed(s)))


if __name__ == '__main__':
    main()