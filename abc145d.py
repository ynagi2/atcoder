def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

def cmb_init(p, n):
    fact = [1, 1]  # fact[n] = (n! mod p)
    factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
    inv = [0, 1]  # factinv 計算用
    for i in range(2, n + 1):
        fact.append((fact[-1] * i) % p)
        inv.append((-inv[p % i] * (p // i)) % p)
        factinv.append((factinv[-1] * inv[-1]) % p)
    return fact, factinv

def cmb(n, r, p):
    fact, factinv = cmb_init(p, n)
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p


def main():
    mod = 10**9 + 7
    x, y = map_int()
    if (x+y) % 3 != 0:
        print(0)
        exit()
    yoko2 = (2*x - y) // 3
    tate2 = (2*y - x) // 3
    if yoko2 < 0 or tate2 < 0:
        print(0)
        exit()

    print(cmb(yoko2 + tate2, min(yoko2, tate2), mod))



if __name__ == '__main__':
    main()