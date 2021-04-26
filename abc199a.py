
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))
# mod = 10**9 + 7

def main():
    a, b, c = map_int()
    if a**2 + b**2 < c**2:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()