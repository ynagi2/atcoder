
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
    n = int(input())
    cnt = 0
    for i in range(n):
        if (i+1) % 2 == 0: continue
        if len(make_divisors(i+1)) == 8:
            cnt += 1
    print(cnt)



if __name__ == '__main__':
    main()