from collections import defaultdict

def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def main():
    a, b = map_int()
    p = defaultdict(int)
    for i in range(a, b+1):
        tmp = make_divisors(i)
        for e in tmp:
            p[e] += 1
    l = []
    for k, v in p.items():
        if v > 1:
            l.append(k)
    l.sort()
    print(l[-1])




if __name__ == '__main__':
    main()