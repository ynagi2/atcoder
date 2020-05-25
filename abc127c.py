n, m = map(int,input().split())
l = []
r = []
for i in range(m):
    a, b = map(int,input().split())
    l.append(a)
    r.append(b)

# 適当に端を設定
a = 1
b = n

# setとか積集合とかでは間に合わない
# となると範囲ではなく限界をmax, minで逐次的に比較し求める
# 最後の結果さえわかればいいので，b-aは最後にするだけ
for i in range(m):
    a = max(l[i], a)
    b = min(r[i], b)

# 負になるケースあるじゃん
if b - a + 1 >= 0:
    print(b - a + 1)
else:
    print(0)