n, m = map(int,input().split())
h = list(map(int,input().split()))

dic = {}
count = 0

# こんなことせずとも，入力のa, bについてその都度どっちが良い展望台か比較，
# よくない方に印していくとよい(t or fを要素とするsize n の配列を用意しておくとかして)

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

for k in dic.keys():
    left = h[k-1]
    right = 0
    for i in dic[k]:
        if h[i-1] >= right:
            right = h[i-1]

    if left > right:
        count += 1

count += n - len(dic)

print(count)