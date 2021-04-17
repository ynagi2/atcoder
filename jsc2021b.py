
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

def main():
    n, m = map_int()
    a = lmap_int()
    b = lmap_int()
    l = set(a)
    for e in b:
        if e in l:
            l.remove(e)
        else:
            l.add(e)
    l = list(l)
    l.sort()
    print(*l)



if __name__ == '__main__':
    main()