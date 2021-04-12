from collections import defaultdict, deque

def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

# g: 二次元配列(あるノードがどのノードと隣接しているかを示す)
# q: キュー
# color: 辺の色
def bfs(g, q, color):
    while q:
        # キューの先頭が現在地
        current = q.popleft()
        c = 1
        # 隣接する各ノードについて
        for node in g[current]:
            if c == color[current]:
                c += 1
            color[node] = c
            c += 1
            q.append(node)
    return color


def main():
    n = int(input())
    g = [[] for i in range(n+1)]
    # 1以外のノードが入る(木の性質より，行数が辺と対応する)
    g_order = []
    for _ in range(n-1):
        x, y = map_int()
        g[x].append(y)
        g_order.append(y)

    # 頂点1を始点としたキュー
    q = deque([1])
    # 各辺の色
    color = [0]*(n+1)
    color = bfs(g, q, color)
    print(max(color))
    for e in g_order:
        print(color[e])



if __name__ == '__main__':
    main()