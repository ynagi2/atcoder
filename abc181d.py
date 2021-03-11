from collections import defaultdict
def main():
    s = input()
    # TLE．8*125=1000より，下三桁のみチェックすればよい
    # ss = defaultdict(int)
    # for e in s:
    #     ss[e] += 1
    # sort_ss = sorted(ss.items(), key=lambda x:x[0], reverse=True)
    # m = ""
    # for e in sort_ss:
    #     m += e[0]*e[1]
    # cnt = 1
    # while True:
    #     i = defaultdict(int)
    #     for e in str(cnt*8):
    #         i[e] += 1
    #     if i == ss:
    #         print("Yes")
    #         break
    #     else:
    #         cnt += 1
    #     if cnt*8 > int(m):
    #         print("No")
    #         break

    # 0がないので，1桁と2桁は別でチェック
    if len(s) < 3:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print("Yes")
            exit()
        else:
            print("No")
            exit()
    
    # ssでcntを再現できたらyes
    cnt = 104
    while cnt < 1000:
        if "0" in str(cnt):
            cnt += 8
            continue
        ss = {}
        for i in range(9):
            ss[str(i+1)] = 0
        for e in s:
            ss[e] += 1
        c = {}
        for i in range(9):
            c[str(i+1)] = 0
        for e in str(cnt):
            c[e] += 1
        for k, v in c.items():
            ss[k] -= v
        f = True
        for v in ss.values():
            if v < 0:
                f = False
        if f:
            print("Yes")
            exit()
        cnt += 8
    print("No")

    




if __name__ == '__main__':
    main()