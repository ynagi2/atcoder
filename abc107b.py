
def main():
    h, w = map(int, input().split())
    a = []
    for _ in range(h):
        tmp = list(input())
        if "#" in tmp:
            a.append(tmp)
    d = []
    for i in range(w):
        f = True
        for j in range(len(a)):
            if a[j][i] == "#":
                f = False
        if f:
            d.append(i)
    ans = []
    for i in range(len(a)):
        s = ""
        for j in range(w):
            if j not in d:
                s += a[i][j]
        ans.append(s)
    for e in ans:
        print(e)



if __name__ == '__main__':
    main()