
def main():
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 0
    # h自体を小さくしていく発想
    while True:
        if max(h) == 0: break
        i = 0
        while i < n:
            if h[i] == 0:
                i += 1
            else:
                cnt += 1
                while h[i] > 0:
                    h[i] -= 1
                    i += 1
                    if i >= n:
                        break
    print(cnt)


if __name__ == '__main__':
    main()