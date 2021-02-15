def main():
    h, w, k = map(int, input().split())
    c = []
    for i in range(h):
        temp = input()
        c.append(temp)
    ans = 0
    # 各塗り方について，各マスをチェック
    for ph in range(2 ** h):
        for pw in range(2 ** w):
            num = 0
            for i in range(h):
                for j in range(w):
                    # 塗られていなくて"#"だったら+1
                    if (ph >> i) & 1 == 0 and (pw >> j) & 1 == 0 and c[i][j] == "#":
                        num += 1
            if num == k:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()