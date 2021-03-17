
def main():
    n = int(input())
    h = list(map(int, input().split()))
    j = 0
    for i in range(len(h)-1):
        if h[i+1] - h[i] <= -2:
            print("No")
            exit()
        if h[i+1] - h[i] == -1:
            j += 1
            if j >= 2:
                print("No")
                exit()
        if h[i+1] - h[i] > 0 and j == 1:
            j -= 1

    print("Yes")

if __name__ == '__main__':
    main()