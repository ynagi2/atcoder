from collections import deque
n, m = map(int,input().split())
dic = {}

for i in range(m):
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

visited = set()
sirube = {}

queue = deque([1])
dist_dic = {}
dist_dic[1] = 0

while len(queue) != 0:
    v = queue.popleft()
    visited.add(v)
    
    for i in dic[v]:
        if i not in visited:
            visited.add(i)
            queue.append(i)
            dist_dic[i] = dist_dic[v] + 1
            sirube[i] = v

print("Yes")

sirube_sorted = sorted(sirube.items(), key=lambda x:x[0])

for i in range(n-1):
    print(sirube_sorted[i][1])