import sys
def main():
    a, b = map(int, input().split())
    k = 1
    cnt = 0

    # 考慮し忘れてWA 反省
    if b == 1:
        print(cnt)
        sys.exit()

    while True:
        k += a-1
        cnt += 1
        if k >= b:
            break

    print(cnt)


if __name__ == '__main__':
    main()