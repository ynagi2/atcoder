
def main():
    a, b, k = map(int, input().split())
    for i in range(a, min(b+1, a+k)):
        print(i)
    for i in range(max(b-k+1, a+k), b+1):
        print(i)

if __name__ == '__main__':
    main()