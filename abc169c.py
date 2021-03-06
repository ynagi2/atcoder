from decimal import Decimal

def main():
    a, b = map(str, input().split())
    a = int(a)
    print(int(a * Decimal(b)))


if __name__ == '__main__':
    main()