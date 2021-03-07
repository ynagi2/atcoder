
def main():
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        c, d = map(int, input().split())
        a.append(c)
        b.append(d)
    ans = 2 * (10 ** 5)
    for i in range(n):
        for j in range(n):
            if i != j:
                ans = min(max(a[i], b[j]), ans)
            else:
                ans = min(a[i]+b[j], ans)
    print(ans)




if __name__ == '__main__':
    main()