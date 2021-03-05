
def main():
    h, w = map(int, input().split())
    n = int(input())
    a = list(map(int, input().split()))

    c = []
    for i in range(h):
        c.append([0]*w)
    row = 0
    col = 0
    for i, e in enumerate(a):
        for _ in range(e):
            c[col][row] = i+1
            row += 1
            if row >= w:
                row = 0
                col += 1
    for i, e in enumerate(c):
        if i % 2 == 0:
            print(' '.join([str(j) for j in e]))
        else:
            print(' '.join([str(j) for j in reversed(e)]))

if __name__ == '__main__':
    main()