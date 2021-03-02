

def main():
    a, b = input().split()
    c = a + b
    c = int(c)
    c = c ** 0.5
    if c.is_integer():
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()