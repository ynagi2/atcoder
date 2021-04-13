
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

# 1.5sec, 10**8になるのでPyPyでないとTLE
def main():
    n = int(input())
    a = lmap_int()
    ans = 0
    for i in range(n):
        m = a[i]
        for j in range(i, n):
            m = min(m, a[j])
            ans = max((j+1-i)*m, ans)
    print(ans)




if __name__ == '__main__':
    main()