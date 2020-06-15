import sys
input = sys.stdin.buffer.readline

def main():
    x = int(input())

    b = 1
    p = 2

    a = []

    # xまで探索すると間に合わない(大分グダった)
    # b ** p でp>=2だから，root(x)までの探索でおkな気がする
    for i in range(int(x ** 0.5) + 1):
        for j in range(int(x ** 0.5) + 1):
            if (b+i) ** (p+j) <= x:
                a.append((b+i) ** (p+j))

    print(max(a))

if __name__ == '__main__':
    main()