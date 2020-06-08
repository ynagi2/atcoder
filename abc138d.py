# 早くなるおまじない
import sys
input = sys.stdin.buffer.readline

# 再帰関数の呼び出し制限
sys.setrecursionlimit(3 * 10 ** 5)

# 深さが一つ前のやつのresの値を足す
# dfsはおk，ここで累積和を使う発想が出てこなかった
# def dfs(node, prev):
#     visited.add(node)
#     if prev != 0:
#         res[node-1] += res[prev-1]
#     for i in dic[node]:
#         if i not in visited:
#             prev = node
#             dfs(i, prev)

def dfs(node, prev, visited, res, dic):
    visited.add(node)
    if prev != 0:
        res[node-1] += res[prev-1]
    for i in dic[node]:
        if i not in visited:
            prev = node
            dfs(i, prev, visited, res, dic)

# 普通に書くよりもこうした方が速くなる
def main():
    n,q = map(int,input().split())

    dic = {}
    for i in range(n-1):
        aa, bb = map(int,input().split())

        if aa not in dic:
            dic[aa] = set()
            dic[aa].add(bb)
        else:
            dic[aa].add(bb)

        if bb not in dic:
            dic[bb] = set()
            dic[bb].add(aa)
        else:
            dic[bb].add(aa)


    p = []
    x = []
    for _ in range(q):
        s, t = map(int,input().split())
        p.append(s)
        x.append(t)

    res = [0]*n
    for i in range(q):
        res[p[i]-1] += x[i]

    visited = set()

    dfs(1, 0, visited, res, dic)
    print(*res, sep=" ")

if __name__ == '__main__':
    main()