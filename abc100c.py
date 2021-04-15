from collections import defaultdict
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

# 普通に2で何回割れるかをシミュレーションするとsqrt(N)ではなくlog(N)でできる
def factorization(n):
    dic = defaultdict(int)
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
    n = int(input())
    a = lmap_int()
    div2 = []
    for e in a:
        dic = factorization(e)
        div2.append(dic[2])
    print(sum(div2))





if __name__ == '__main__':
    main()