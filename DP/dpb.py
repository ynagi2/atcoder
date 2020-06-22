import sys
input = sys.stdin.buffer.readline

def main():
    n, k = map(int,input().split())
    h = list(map(int,input().split()))

    dp = [0]*n

    dp[1] = abs(h[1] - h[0])
    for i in range(2, n):
        dp[i] = dp[i-1] + abs(h[i] - h[i-1])
        for j in range(2, k+1):
            # これ入れないとh[-1]とか参照はじめちゃう
            if i-j < 0:
                continue
            dp[i] = min(dp[i-j] + abs(h[i] - h[i-j]), dp[i])

    print(dp[-1])



if __name__ == '__main__':
    main()