import sys
input = sys.stdin.buffer.readline

def main():
    n, m, k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    asum = [0]*(n+1)
    bsum = [0]*(m+1)

    for i in range(n):
        asum[i+1] = asum[i] + a[i]

    for i in range(m):
        bsum[i+1] = bsum[i] + b[i]

    # jを小さくしていく発想がなかった
    j = m
    res = 0
    for i in range(n+1):
        # asumの分岐をさせてからbsumとの和を考えていく
        if asum[i] > k:
            break
        while asum[i] + bsum[j] > k:
            j -= 1
        
        res = max(res, j+i)
    print(res)


if __name__ == '__main__':
    main()