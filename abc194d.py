
# 等差×等比の部分和求めて極限とばすと，
# n / n-k をk=1からn-1まで足し合わせればいいことがわかる
# 別の考え方として，E = p*1 + (1-p)(E+1)
# (確率pで成功し，1-pでEが1回増えるという関係式)
# より，E = 1/p が求まるので，p = 1 - n/Nから，
# N / N-n の総和を求めればよいと考えられる
def main():
    n = int(input())
    ans = 0
    for i in range(n-1):
        ans += n / (i+1)
    print(ans)


if __name__ == '__main__':
    main()