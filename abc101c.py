import math

def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))
# mod = 10**9 + 7

def main():
    n, k = map_int()
    a = lmap_int()
    one_index = a.index(1)
    ans = 0
    ans += math.ceil(((n-1) - one_index) / (k-1) + one_index / (k-1))
    print(ans)




if __name__ == '__main__':
    main()