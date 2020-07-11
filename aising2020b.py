def main():
    n = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    for i, e in enumerate(a):
        if (i+1) % 2 == 1 and e % 2 == 1:
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()