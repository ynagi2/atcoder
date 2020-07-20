
def main():
    n = int(input())
    b = list(map(int, input().split()))

    a = [0]*n

    # a[0]とa[-1]に関しては不等式による制約は1つしかないので最大は自動的に決まる
    for i,e in enumerate(b):
        if i == 0:
            a[0] = b[0]
        # 例えばa[1]なら，a[1] <= b[0] and max(a[1], a[2]) <= b[1]
        # したがって，a[1] = min(b[0], b[1])
        # 上式に気づくまでに時間がかかった
        else:
            a[i] = min(b[i-1], b[i])

    a[-1] = b[-1]

    print(sum(a))

if __name__ == '__main__':
    main()