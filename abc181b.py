def souwa(n):
    return 0.5 * n * (n+1)

def main():
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    ans = 0
    for i in range(n):
        ans += souwa(b[i]) - souwa(a[i] - 1)
    print(int(ans))



if __name__ == '__main__':
    main()