
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

def main():
    n = int(input())
    s = input()
    ans = ""
    l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for e in s:
        idx = l.index(e)
        ans += l[(idx + n) % len(l)]
    print(ans)



if __name__ == '__main__':
    main()