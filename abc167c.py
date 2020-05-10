n, m, x = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))

# 再帰を使ってDFSする方法も汎用的(ここではbit全探索した)
price = {}
for i in range(2 ** n):
    rikai = []
    total = 0
    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う(1なら買う)
            rikai.append(a[j][1:])  # フラグが立っていたら bag に果物を詰める
            total += a[j][0]  # 買い物累計額にも加算
    price[total] = rikai


def python_list_add(in1, in2):
   return list(map(sum, zip(in1, in2)))

flag = False
minp = (10 ** 5) * 12
for k,v in price.items():
    r = [0]*m
    for i in range(len(v)):
        r = python_list_add(r, v[i])
    if min(r) >= x:
        minp = min(minp, k)
        flag = True

if flag:
    print(minp)
else:
    print("-1")
