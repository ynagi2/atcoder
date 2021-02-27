from bisect import bisect, bisect_left


def main():
    n = int(input())
    l = list(map(int, input().split()))
    l = sorted(l)
    cnt = 0

    for a in range(1, n):
        for b in range(a):
            c = bisect_left(l, l[b] + l[a])
            cnt += c - a - 1
    print(cnt)

if __name__ == '__main__':
    main()