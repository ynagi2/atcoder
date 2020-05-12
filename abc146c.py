a, b, x = map(int,input().split())

ok = 0
ng = 10 ** 9 + 1

# 条件を満たしていればTrue, そうでなければFalseを返す関数ということ
def is_ok(n):
   return a*n + b*len(str(n)) <= x

while ng-ok > 1:
    mid = int((ok+ng) / 2) # 平均(小数切り捨て)
    if is_ok(mid):
        # midがokなら，okをmidまで持ってくる
        ok = mid
    else:
        # midがngなら，ngをmidまで持ってくる
    	ng = mid

print(ok)