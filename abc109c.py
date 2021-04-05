
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def main():
    n, x = map_int()
    x_loc = lmap_int()

    if n == 1:
        print(abs(x - x_loc[0]))
        exit()

    ans = abs(x - x_loc[0])
    for i in range(n-1):
        ans = gcd(ans, abs(x - x_loc[i+1]))
    print(ans)



if __name__ == '__main__':
    main()