
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))
# mod = 10**9 + 7

def main():
    r1, c1 = map_int()
    r2, c2 = map_int()

    if r1 == r2 and c1 == c2:
        print(0)
    elif r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
    elif (r1 + c1) % 2 == (r2 + c2) % 2 or (r1 + c1 - 3 <= r2 + c2 and r2 + c2 <= r1 + c1 + 3) or (r1 - c1 - 3 <= r2 - c2 and r2 - c2 <= r1 - c1 + 3) or abs(r1 - r2) + abs(c1 - c2) <= 6:
        print(2)
    else:
        print(3)

if __name__ == '__main__':
    main()