
# 何故かわかっていないが，辞書でソートだとWAでリストでソートだとACになる
def main():
    n, m = map(int, input().split())
    ab = []
    for _ in range(n):
        x, y = map(int, input().split())
        ab.append((x, y))
    # dic_sorted = sorted(dic.items(), key=lambda x:x[0])
    ab.sort()
    ans = 0
    cnt = 0
    for i in range(n):
        if m == cnt: break
        if m < cnt + ab[i][1]:
            ans += ab[i][0] * (m - cnt)
            break
        else:
            ans += ab[i][0] * ab[i][1]
            cnt += ab[i][1]

    # for i in range(n):
    #     if m == cnt: break
    #     if m < cnt + dic_sorted[i][1]:
    #         ans += dic_sorted[i][0] * (m - cnt)
    #         break
    #     else:
    #         ans += dic_sorted[i][0] * dic_sorted[i][1]
    #         cnt += dic_sorted[i][1]
    print(ans)


if __name__ == '__main__':
    main()