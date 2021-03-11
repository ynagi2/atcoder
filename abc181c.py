
def main():
    n = int(input())
    x = []
    y = []
    for _ in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if x[i] - x[j] == 0 and x[j] - x[k] == 0:
                    print("Yes")
                    exit()
                if x[i] - x[j] == 0 or x[j] - x[k] == 0:
                    continue
                if (y[j] - y[i]) / (x[j] - x[i]) == (y[k] - y[j]) / (x[k] - x[j]):
                    print("Yes")
                    exit()
    print("No")



if __name__ == '__main__':
    main()