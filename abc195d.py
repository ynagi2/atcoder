
def main():
    n, m, q = map(int, input().split())
    w = []
    v = []
    for i in range(n):
        z,y = map(int,input().split())
        w.append(z)
        v.append(y)
    x = list(map(int, input().split()))
    l = []
    r = []
    for i in range(q):
        z,y = map(int,input().split())
        l.append(z)
        r.append(y)
    ux = []
    for i in range(q):
        tmp_x = []
        for j, e in enumerate(x):
            if j+1 >= l[i] and j+1 <= r[i]:
                tmp_x.append(0)
            else:
                tmp_x.append(e)
        tmp_x.sort()
        ux.append(tmp_x)

    for i in range(q):
        ans = 0
        used = set()
        for each_x in ux[i]:
            tmp_val = 0
            idx = -1
            for k in range(n):
                if w[k] > each_x or k in used:
                    continue
                if v[k] > tmp_val:
                    tmp_val = v[k]
                    idx = k
            used.add(idx)
            ans += tmp_val
        print(ans)


if __name__ == '__main__':
    main()