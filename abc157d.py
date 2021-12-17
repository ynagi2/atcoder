from collections import defaultdict, deque
from itertools import permutations, combinations
from math import factorial, ceil, floor
from decimal import Decimal
import heapq

def iipt(): return int(input())
def map_str(): return input().split()
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))
# mod = 10**9 + 7


class UnionFind():
    # 最初各要素はバラバラ(リストの各indexは-1とする)
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    # xが属するグループの根を返す
    # 再帰的にfindすることで根(負の値を持つparentsの要素)を探す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # xが属するグループとyが属するグループを併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    # xが属するグループの要素数を返す
    def size(self, x):
        return -self.parents[self.find(x)]

    # xとyが同じグループに属するかを返す
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # xが属するグループに属する要素をリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    # すべての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    # グループの数を返す
    def group_count(self):
        return len(self.roots())

    # {ルート要素: [そのグループに含まれる要素のリスト], ...}のdefaultdictを返す
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    # ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す(print()での表示がこれ)
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():
    n, m, k = map_int()
    a, b, c, d = [], [], [], []
    friends = defaultdict(set)
    blocks = defaultdict(set)
    for _ in range(m):
        x, y = map_int()
        a.append(x-1)
        b.append(y-1)
        friends[x-1].add(y-1)
        friends[y-1].add(x-1)
    uf = UnionFind(n)
    for i in range(m):
        uf.union(a[i], b[i])
    for _ in range(k):
        x, y = map_int()
        c.append(x-1)
        d.append(y-1)
        # friendsはみんな同じグループにいるはずだが，blocksは同じ場合と違う場合があるので，一緒なら引く
        if uf.same(x-1, y-1):
            blocks[x-1].add(y-1)
            blocks[y-1].add(x-1)
    ans = []
    for i in range(n):
        val = uf.size(i) - len(friends[i]) - len(blocks[i]) - 1
        ans.append(val)
    print(*ans)


if __name__ == '__main__':
    main()