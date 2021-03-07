
# abs(a_i) <= 200から，出てきた各値の数をカウントするのが想定解法らしい
def main():
    n = int(input())
    ans = 0
    a = list(map(int, input().split()))
    asum = [0]*(n+1)
    for i in range(n):
        asum[i+1] = asum[i] + a[i]
    for i in range(n):
        ans += (n-1) * (a[i] ** 2)
    tmp = 0
    for i in range(n):
        tmp += a[i] * (asum[n] - asum[i+1])
    ans = ans -2 * tmp
    print(ans)



if __name__ == '__main__':
    main()