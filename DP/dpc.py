import sys
input = sys.stdin.buffer.readline

def main():
    n = int(input())
    abc = [list(map(int, input().split())) for _ in range(n)]

    dp = [0]*(n+1)
    for x in range(n+1):
        dp[x] = [0, 0, 0]

    for i in range(1, n+1):
        for j in range(3):
            for k in range(3):
                if j != k:
                    dp[i][k] = max(dp[i][k], dp[i-1][j] + abc[i-1][k])

    ans = 0
    for i in range(3):
        ans = max(ans, dp[n][i])
    print(ans)

if __name__ == '__main__':
    main()