
def main():
    n, m, t = map(int, input().split())
    a = []
    b = []
    for _ in range(m):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    bat = n
    for i in range(m):
        if i != 0:
            bat = bat - (a[i] - b[i-1])
        else:
            bat = bat - a[i]
        if bat <= 0:
            print("No")
            exit()
        bat = bat + b[i] - a[i]
        if bat > n:
            bat = n
    bat = bat - (t - b[-1])
    print("No") if bat <= 0 else print("Yes")



if __name__ == '__main__':
    main()