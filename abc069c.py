
def main():
    n = int(input())
    a = list(map(int, input().split()))

    c = 0
    o = 0
    two = 0
    for e in a:
        if e % 4 == 0:
            c += 1
        if e % 2 == 1:
            o += 1
        if e % 2 == 0 and e % 4 != 0:
            two += 1
    if two == 0 and o - c <= 1:
        print("Yes")
        exit()
    # 両隣に奇数が来たらだめという点で，
    # 連続したtwoは奇数1つと置換可能
    if c >= o:
        print("Yes")
        exit()
    print("No")


if __name__ == '__main__':
    main()