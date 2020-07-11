def main():
    l, r, d = map(int, input().split())
    
    cnt = 0
    for i in range(l, r+1):
        if i % d == 0:
            cnt += 1

    print(cnt)



if __name__ == '__main__':
    main()