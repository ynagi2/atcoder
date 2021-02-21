def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors, upper_divisors[::-1]

def main():
    n = int(input())
    low, upper = make_divisors(n)
    f = int(max(low[-1], n / low[-1]))
    print(len(str(f)))
    
if __name__ == '__main__':
    main()