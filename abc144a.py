
def main():
    a, b = map(int, input().split())
    if a >= 10 or b >= 10:
        print(-1)
    else:
        print(a*b)



if __name__ == '__main__':
    main()