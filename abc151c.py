n, m = map(int,input().split())
p = []
s = []
for _ in range(m):
    temp = input().split()
    p.append(int(temp[0]))
    s.append(temp[1])

ac = 0
# penaは配列にして各問題について数える
  # acを出さなかった問題についてはペナ数をカウントしないから？
pena = [0]*n
flag = [False]*n

# 普通にこんがらがった
for pe, se in zip(p, s):
    if se == "AC":
        flag[pe-1] = True
    else:
        if flag[pe-1] is False:
            pena[pe-1] += 1

psum = 0
for i in range(n):
    if flag[i]:
        ac += 1
        psum += pena[i]

print(ac, psum)