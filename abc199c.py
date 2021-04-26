def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))
# mod = 10**9 + 7

def main():
    n = int(input())
    s = list(input())
    q = int(input())
    t, a, b = [], [], []
    for i in range(q):
        x, y, z = map_int()
        t.append(x)
        a.append(y)
        b.append(z)
    f = False
    # fをTrueにしたときを+-nで表現する発想が出てこなかった
    for i in range(q):
        if t[i] == 1 and not(f):
            tmp = s[a[i]-1]
            s[a[i]-1] = s[b[i]-1]
            s[b[i]-1] = tmp
        elif t[i] == 1 and f:
            if a[i] <= n:
                val = a[i]-1+n
            else:
                val = a[i]-1-n
            tmp = s[val]
            if b[i] <= n:
                s[val] = s[b[i]-1+n]
                s[b[i]-1+n] = tmp
            else:
                s[val] = s[b[i]-1-n]
                s[b[i]-1-n] = tmp
        else:
            if f:
                f = False
            else:
                f = True
    if f:
        print(''.join(s[n:] + s[:n]))
    else:
        print(''.join(s))



if __name__ == '__main__':
    main()