
def main():
    x, k, d = map(int, input().split())

    if x == 0:
        if k % 2 == 0:
            print(0)
        else:
            print(d)
        exit()

    t = abs(x) // d + 1
    if x > 0:
        fir = x - t * d
        if k <= t:
            print(abs(x - k * d))
        elif (k - t) % 2 == 0:
            print(abs(fir))
        else:
            print(abs(fir + d))
        exit()
    else:
        fir = x + t * d
        if k <= t:
            print(abs(x + k * d))
        elif (k - t) % 2 == 0:
            print(abs(fir))
        else:
            print(abs(fir - d))
        exit()



if __name__ == '__main__':
    main()