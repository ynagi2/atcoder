from collections import defaultdict

def factorization(n, dic):
    a = 2
    while a * a <= n:
        if n % a != 0:
            a += 1
            continue
        ex = 0
        while n % a == 0:
            ex += 1
            n /= a
        dic[a] += ex
        a += 1
    if n != 1: dic[n] += 1
    return dic


# 普通にやるとn!の素因数分解が終わらない
# →1~Nのfactorizationを足し合わせる
def main():
    n = int(input())
    dic = defaultdict(int)
    for i in range(n):
        dic = factorization(i+1, dic)
    num = 1
    for v in dic.values():
        num *= (v + 1)
    print(num % (10 ** 9 + 7))

if __name__ == '__main__':
    main()
