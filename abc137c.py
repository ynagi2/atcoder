from collections import defaultdict
from itertools import combinations

def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

# こんなことせずとも逐一ソートした入力をdictに入れ，現れた回数をansに足していくと楽
def main():
    n = int(input())
    s = []
    for _ in range(n):
        tmp = input()
        tmp = sorted(tmp)
        s.append(''.join(tmp))
    s.sort()
    ans = 0
    cnt = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            cnt += 1
        else:
            ans += cnt * (cnt + 1) // 2
            cnt = 0
    if cnt != 0:
        ans += cnt * (cnt + 1) // 2
    print(ans)

if __name__ == '__main__':
    main()