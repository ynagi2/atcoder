
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))
# mod = 10**9 + 7

def main():
    n = int(input())
    a = lmap_int()
    b = lmap_int()
    for i in range(n):
        if i == 0:
            ans = set()
            for j in range(b[i] - a[i] + 1):
                ans.add(j+a[i])
        else:
            tmp = set()
            for e in ans:
                if not(e >= a[i] and e <= b[i]):
                    tmp.add(e)
            ans = ans - tmp
    print(len(ans))

if __name__ == '__main__':
    main()