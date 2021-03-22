
def main():
    n, m = map(int, input().split())
    s, c = [], []
    for _ in range(m):
        a, b = map(int, input().split())
        s.append(a)
        c.append(b)
    
    for i in range(1000):
        p = True
        for j in range(m):
            if i < 10 and (2 in s or 3 in s):
                p = False
                break
            if 10 <= i and i < 100 and (3 in s):
                p = False
                break
            if str(i)[s[j]-1] != str(c[j]):
                p = False
        if p and len(str(i)) == n:
            print(i)
            exit()
    print(-1)


if __name__ == '__main__':
    main()