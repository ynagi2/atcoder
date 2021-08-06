import sys
from collections import defaultdict, deque
from itertools import permutations, combinations
from math import factorial, ceil, floor
from decimal import Decimal

def i_input(): return int(input())
def map_str(): return input().split()
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))


# g: 二次元配列(あるノードがどのノードと隣接しているかを示す)
# q: キュー
def bfs(n, g, q, dist):
    cnt = [0]*n
    cnt[0] = 1
    mod = 10**9 + 7
    while q:
        # キューの先頭が現在地
        current = q.popleft()
        # 隣接する各ノードについて
        # cntで経路数を記録していく(1つ前のノードの経路数を引き継いでいく)
        for node in g[current]:
            if dist[node] == 0:
                dist[node] = dist[current] + 1
                cnt[node] = cnt[current]
                q.append(node)
            elif dist[node] == dist[current] + 1:
                cnt[node] = (cnt[node] + cnt[current]) % mod
    return dist, cnt


def main():
    sys.setrecursionlimit(3 * 10 ** 5)
    n, m = map_int()
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map_int()
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    q = deque([0])
    dist = [0]*n
    dist, cnt = bfs(n, g, q, dist)
    print(cnt[-1])



if __name__ == '__main__':
    main()