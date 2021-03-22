
def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = [0]*n
    for e in a:
        ans[e-1] += 1
    for e in ans:
        print(e)





if __name__ == '__main__':
    main()