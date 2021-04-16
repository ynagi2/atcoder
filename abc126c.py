import math

def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

# 実際にコイン投げをして値を得てもO(NlogK)で間に合う
def main():
    n, k = map_int()
    ans = 0
    if k == 1:
        print(1)
        exit()
    for i in range(n):
        val = (math.log(k-1) - math.log(i+1)) // math.log(2)
        if val < 0:
            x = 0
        else:
            x = val + 1
        ans += 0.5 ** x
    print(ans / n)



if __name__ == '__main__':
    main()