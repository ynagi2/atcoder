

def main():
    n = int(input())
    apx = [map(int, input().split()) for _ in range(n)]
    a, p, x = [list(i) for i in zip(*apx)]

    ans = 10 ** 9 + 1
    for i in range(n):
        if x[i] > a[i]:
            ans = min(ans, p[i])

    if ans == 10 ** 9 + 1:
        ans = -1
    print(ans)

if __name__ == '__main__':
    main()