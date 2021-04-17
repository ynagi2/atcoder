
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

# 単にA1から順に条件を満たす樹形図をかけばよい(樹形図の発想がなかった)
# あまりを取る場合は，**ではなくpowで計算したほうが早いときがあるらしい
def main():
    n, p = map_int()
    mod = 10**9 + 7
    ans = (p-1) * (pow(p-2, n-1, mod)) % mod
    print(ans)

if __name__ == '__main__':
    main()