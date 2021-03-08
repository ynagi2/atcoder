
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    if n == m:
        print(0)
        exit()
    if m == 0:
        print(1)
        exit()

    w = []
    if a[0] - 1 > 0: w.append(a[0] - 1)
    for i in range(len(a)-1):
        if a[i+1] - a[i] - 1 > 0: w.append(a[i+1] - a[i] - 1)
    if n - a[-1] > 0: w.append(n - a[-1])
    k = min(w)
    cnt = 0
    for i in w:
        if i % k == 0:
            cnt += i//k
        else:
            cnt += i//k + 1
    print(int(cnt))


if __name__ == '__main__':
    main()