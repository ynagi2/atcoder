
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

def is_ok(a, b, x, n):
    return a*n + b*len(str(n)) <= x

def main():
    a, b, x = map_int()

    ok = 0
    ng = 10 ** 9 + 1

    while ng - ok > 1:
        mid = (ok + ng) // 2
        if is_ok(a, b, x, mid):
            ok = mid
        else:
            ng = mid
    print(ok)



if __name__ == '__main__':
    main()