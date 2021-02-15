def main():
    x = int(input())
    # 151 ** 5 - 150 ** 5 > 10 ** 9
    # したがって，プラマイ151くらいで調べればいい
    for a in range(-151, 151):
        for b in range(-151, 151):
            if a ** 5 - b ** 5 == x:
                print("{} {}".format(a, b))
                exit(0)


if __name__ == '__main__':
    main()