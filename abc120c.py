
def main():
    s = input()
    zero = 0
    one = 0
    for e in s:
        if e == "0":
            zero += 1
        else:
            one += 1
    print(min(zero, one)*2)


if __name__ == '__main__':
    main()