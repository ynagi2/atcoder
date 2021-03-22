
def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for _ in range(n):
        y, z = map(int, input().split())
        v.append(y)
        p.append(z)
    s = 0
    ans = -1
    for i in range(n):
        s += v[i] * p[i]
        if s > x*100:
            ans = i+1
            print(ans)
            exit()
    print(ans)


if __name__ == '__main__':
    main()