def main():
    t = int(input())
    l = []
    r = []
    for i in range(t):
        a, b = map(int, input().split())
        l.append(a)
        r.append(b)
    for i in range(t):
        if r[i] - l[i] < l[i]:
            print(0)
        else:
            num = r[i] - l[i] - l[i] + 1
            print(int(num * (num + 1) / 2))

if __name__ == '__main__':
    main()