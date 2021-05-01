
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))
# mod = 10**9 + 7

def main():
    n, D, H = map_int()
    d, h = [], []
    for i in range(n):
        x, y = map_int()
        d.append(x)
        h.append(y)
    ans = 0
    for i in range(n):
        tmp = H - D*(H-h[i]) / (D-d[i])
        if tmp < 0:
            tmp = 0
        ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()