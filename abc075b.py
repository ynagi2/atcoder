h, w = map(int, input().split())
temp = [input() for _ in range(h)]

s = [[""]*w for _ in range(h)]

# python, list(文字列)とすれば1文字ずつを要素とするlistができる
# 別に文字列のまま扱ってもよさそう
for i in range(h):
    s[i] = list(temp[i])

ns = [[0]*w for _ in range(h)]

# 文字列がタプル同様あとから変更できない仕様に悩まされた
# 文字列として受け取るのではなく，リストで最初から受け取ればよい

# なんでこれリストnsがまとめて書き換わってしまうんだ
# -> https://note.nkmk.me/python-list-initialize/
  # 要素のリストがすべて同じオブジェクトになってしまっているらしい
  # s, nsを内包表記で書く必要がある
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            ns[i][j] = "#"

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            
            if i != 0:
                if ns[i-1][j] != "#": ns[i-1][j] += 1
                if j != 0:
                    if ns[i-1][j-1] != "#": ns[i-1][j-1] += 1
                if j != w-1:
                    if ns[i-1][j+1] != "#": ns[i-1][j+1] += 1
                
            if j != 0:
                if ns[i][j-1] != "#": ns[i][j-1] += 1
            if j != w-1:
                if ns[i][j+1] != "#": ns[i][j+1] += 1

            if i != h-1:
                if ns[i+1][j] != "#": ns[i+1][j] += 1
                if j != 0:
                    if ns[i+1][j-1] != "#": ns[i+1][j-1] += 1
                if j != w-1:
                    if ns[i+1][j+1] != "#": ns[i+1][j+1] += 1

for i in range(h):
    for j in range(w):
        ns[i][j] = str(ns[i][j])

for i in range(h):
    print("".join(ns[i]))