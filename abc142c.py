def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = [0]*n
    for i, e in enumerate(a):
        ans[e-1] = i+1
    print(' '.join([str(i) for i in ans]))

if __name__ == '__main__':
    main()