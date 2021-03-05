# pypyにする
def main():
    n, m, Q = map(int, input().split())
    lr = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        l, r = map(int, input().split())
        lr[l][r] += 1

    p = []
    for _ in range(Q):
        _list = list(map(int, input().split()))
        p.append(_list)

    sums = []
    for l in lr:
        csum = [0]*(n+2)
        for i in range(n):
            # lrは0~nで始めているので，今回はl[i+1]で足す
            csum[i+1] = csum[i] + l[i+1]
        sums.append(csum)

    for e in p:
        ans = 0
        l, r = e[0], e[1]
        # 与えられた区間内での計算
        for c in sums[l:r+1]:
            ans += (c[r] - c[l-1])
        print (ans)


if __name__ == '__main__':
    main()