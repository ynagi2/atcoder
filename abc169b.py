
# 2**63 - 1 (1.8* 10**19)以上の値はとれない
def main():
    n = int(input())
    a = list(map(int, input().split()))

    tmp = None
    for i, e in enumerate(a):
        if i == 0:
            ans = e
        else:
            ans *= e
        if ans > 10 ** 18:
            tmp = i
            break
    if tmp == i and 0 not in a[tmp+1:]:
        print(-1)
        exit()
    if tmp == i and 0 in a[tmp+1:]:
        print(0)
        exit()
    print(ans)

if __name__ == '__main__':
    main()