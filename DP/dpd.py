import sys
input = sys.stdin.buffer.readline

def main():
    n, w = map(int,input().split())
    wei = []
    val = []
    for i in range(n):
        a, b = map(int,input().split())
        wei.append(a)
        val.append(b)

    dp = [[0 for i in range(w+1)] for j in range(n+1)]

    for i in range(n):
        for sum_w in range(w+1):
            # i 番目の品物を選ぶ場合
            if sum_w - wei[i] >= 0:
                dp[i+1][sum_w] = max(dp[i+1][sum_w], dp[i][sum_w - wei[i]] + val[i])

            # i 番目の品物を選ばない場合
            dp[i+1][sum_w] = max(dp[i+1][sum_w], dp[i][sum_w])

    print(dp[n][w])


if __name__ == '__main__':
    main()