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
    n = int(input())
    t = []
    for _ in range(n):
        tmp = int(input())
        t.append(tmp)
    ans = 1
    for e in t:
        a = gcd(ans, e)
        ans = ans * e // a # ここをint()で切り捨てするとWA．なぜ？
    print(ans)



if __name__ == '__main__':
    main()