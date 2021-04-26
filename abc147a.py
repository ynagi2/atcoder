
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))
# mod = 10**9 + 7

def main():
    a1, a2, a3 = map_int()
    if a1 + a2 + a3 <= 21:
        print("win")
    else:
        print("bust")


if __name__ == '__main__':
    main()