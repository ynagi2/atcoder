def main():
    n = int(input())

    # int()だと全体を丸めないといけないことに注意
    # * 0.5 とかもよくない
    print(((n-1) * n) // 2)

if __name__ == '__main__':
    main()