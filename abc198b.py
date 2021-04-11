
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

def main():
    n = int(input())
    a = str(n)[::-1]
    cnt = 0
    for e in a:
        if e != "0":
            break
        else:
            cnt += 1
    b = a[cnt:]
    s = b[::-1]
    if s == s[::-1]:
        print("Yes")
    else:
        print("No")



if __name__ == '__main__':
    main()