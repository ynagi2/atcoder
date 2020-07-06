import sys
input = sys.stdin.buffer.readline

def main():
    n = int(input())
    a = n // 1000

    if n % 1000 != 0:
        print((a+1)*1000 - n)
    else:
        print(0)

if __name__ == '__main__':
    main()