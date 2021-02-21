def main():
    n, k = map(int, input().split())
    a = n
    for i in range(k):
        g1 = sorted(str(a), reverse=True)
        g1 = int(''.join(g1))
        g2 = sorted(str(a))
        g2 = int(''.join(g2))
        a = g1 - g2
    print(a)

if __name__ == '__main__':
    main()