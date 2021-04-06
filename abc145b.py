
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

def main():
    n = int(input())
    s = input()
    if n % 2 == 1:
        print("No")
    else:
        t = int(n/2)
        if s[:t] == s[t:]:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()