def is_ok(n, m, x):
    ans = 0
    di = len(x)    
    for i,e in enumerate(x):
        ans += n**(di-i-1) * int(e)
    return ans <= m

def main():
    x = input()
    m = int(input())
    d = 0
    for s in x:
        d = max(d, int(s))

    # xが1桁のときは答えは0 or 1
    if len(x) == 1:
        print(1 if d <= m else 0)
        exit()

    ok = 0
    # 上限
    ng = 10 ** 18 + 1

    while ng-ok > 1:
        mid = (ok+ng) // 2 # 平均(小数切り捨て)
        if is_ok(mid, m, x):
            # midがokなら，okをmidまで持ってくる
            ok = mid
        else:
            # midがngなら，ngをmidまで持ってくる
            ng = mid

    print(max(0, ok - d))

    # これではd+1進数から順に見ていくことになり，O(N)となるため間に合わなかった
    # while True:
    #     ans = 0
    #     di = len(x)
    #     for i,e in enumerate(x):
    #         ans += n**(di-i-1) * int(e)
    #     if ans <= m:
    #         cnt += 1
    #         n += 1
    #     else:
    #         break
    # print(cnt)


if __name__ == '__main__':
    main()