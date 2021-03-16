def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors, upper_divisors

def main():
    n = int(input())
    lower, upper = make_divisors(n)
    ans = 10**12
    if len(lower) > len(upper):
        walk = lower[-1] - 1 + lower[-1] - 1
        ans = min(ans, walk)
    for i in range(len(upper)):
        walk = lower[i] - 1 + upper[i] - 1
        ans = min(ans, walk)
    print(ans)




if __name__ == '__main__':
    main()