def main():
    n = int(input())
    arr = [i+1 for i in range(n)]

    if n % 2 == 0:
        print(0.5)
    else:
        print((n//2 + 1) / n)

if __name__ == '__main__':
    main()