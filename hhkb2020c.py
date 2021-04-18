
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

# iは単調増加
def main():
    n = int(input())
    p = lmap_int()
    i = 0
    s = set()
    for e in p:
        s.add(e)
        while True:
            if i not in s:
                print(i)
                break
            else:
                i += 1


if __name__ == '__main__':
    main()