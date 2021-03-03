def factorization(n):
    dic = {}
    a = 2
    while a * a <= n:
        if n % a != 0:
            a += 1
            continue
        ex = 0
        while n % a == 0:
            ex += 1
            n /= a
        dic[a] = ex
        a += 1
    if n != 1: dic[int(n)] = 1
    return dic


def main():
    n, p = map(int, input().split())
    div = factorization(p)
    ans = 1
    # 各素因数を振り分ける
    # 割ればa_iをそれぞれ記述する必要はない
    for k, v in div.items():
        if v >= n:
            ans *= k ** (v // n)
    print(ans)


if __name__ == '__main__':
    main()