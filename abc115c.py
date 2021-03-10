
def main():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]

    h.sort()
    ans = 10 ** 9 - 1
    for i in range(len(h)-(k-1)):
        ans = min(h[i+k-1] - h[i], ans)
    print(ans)


if __name__ == '__main__':
    main()