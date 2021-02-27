
def main():
    n = int(input())
    d = list(map(int, input().split()))
    s = 0
    for i in range(len(d)):
        for j in range(len(d) - i - 1):
            s += d[i] * d[i+j+1]
    print(s)



if __name__ == '__main__':
    main()