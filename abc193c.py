

def main():
    n = int(input())
    ln = int(n ** 0.5)
    s = set()
    if ln < 2:
        print(n)
    else:
        for i in range(ln - 1):
            b = 2
            while True:
                if (i+2) ** b <= n:
                    s.add((i+2) ** b)
                    b += 1
                else:
                    break
        print(n - len(s))


if __name__ == '__main__':
    main()