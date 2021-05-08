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

# 今回はあまりが一致さえしていればいいので，鳩ノ巣原理より．201パターン調べれば必ずyesの組合せが出てくる
def main():
    n = i_input()
    a = lmap_int()
    search = min(8, n)

    ans = {}
    for i in range(2**search-1):
        string = str(bin(2**search-(i+1))[2:])
        if len(string) < search:
            string = '0'*(search - len(string)) + string
        tf = []
        for z in range(search):
            tf.append(int(string[z]))
        val = 0
        idxs = []
        for j in range(search):
            if tf[j] == 1:
                val += a[j]
                idxs.append(j+1)
        val = val % 200
        if val not in ans:
            ans[val] = idxs
        else:
            print("Yes")
            tmp1 = ' '.join([str(e) for e in idxs])
            tmp2 = ' '.join(str(e) for e in ans[val])
            print("{} {}".format(len(idxs), tmp1))
            print("{} {}".format(len(ans[val]), tmp2))
            exit()
    
    print("No")


if __name__ == '__main__':
    main()