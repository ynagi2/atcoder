kn = list(map(int,input().split()))
a = list(map(int,input().split()))

k = kn[0]
n = kn[1]


dis = []

for i in range(n):
    if i == 0:
        # +a[0] が抜けていることにしばらく気が付かなかった
        # 入力例以外も試すようにする
        dis.append(min((a[n-1] - a[0]), (k - a[n-1] + a[0])))
    else:
        dis.append(min((a[i] - a[i-1]), (k - a[i] + a[i-1])))

del dis[dis.index(max(dis))]

print(sum(dis))