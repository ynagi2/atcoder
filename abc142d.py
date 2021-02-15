def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def factorization(n):
    """nを素因数分解"""
    """2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""
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
    # 最大公約数もとめて，それの素因数を1つずつ選べばいいだけ
    a, b = map(int, input().split())
    g = gcd(a, b)
    arr = factorization(g)
    if g == 1:
        print(1)
    else:
        print(len(arr) + 1)

if __name__ == '__main__':
    main()