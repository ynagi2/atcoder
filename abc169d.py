def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr


def main():
    n = int(input())
    cnt = 0
    a = factorization(n)
    # n <= 10 ** 12から，素因数の指数は43以下
    b = [1, 3, 6, 10, 15, 21, 28, 36, 43]
    if len(a) == 1 and a[0][0] == 1:
        print(0)
    else:
        # 各素因数について，
        for e in a:
            # 何回その素因数で割れるか
            for j in range(len(b)):
                if e[1] < b[j]:
                    cnt += j
                    break
        print(cnt)



if __name__ == '__main__':
    main()