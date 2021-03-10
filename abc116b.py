
def main():
    s = int(input())
    i = 1
    a = []
    while True:
        if i == 1:
            a.append(s)
        else:
            if a[-1] % 2 == 0:
                c = a[-1] / 2
            else:
                c = 3 * a[-1] + 1
            a.append(c)
            if c in a[:-1]:
                print(len(a))
                break
        i += 1



if __name__ == '__main__':
    main()