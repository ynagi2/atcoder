
def main():
    a, k = map(int, input().split())
    day = 0
    # k = 1 でも等比級数的に増加するので，k = 0だけ分ければよい
    # 等比級数の和の公式から二分探索しようとしてしまった
    if k == 0:
        print(2 * 10**12 - a)
    else:
        while True:
            if a >= 2 * 10**12:
                print(day)
                break
            a = a + 1 + k*a
            day += 1



if __name__ == '__main__':
    main()