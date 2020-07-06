# https://qiita.com/drken/items/dc53c683d6de8aeacf5a#e-%E5%95%8F%E9%A1%8C---knapsack-2
# 上記をそのまま書いたつもりのコードが通らなくて困惑
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

    max_v = 10**5 + 10
    dp = [[float('inf') for i in range(max_v)] for j in range(100+10)]

    dp[0][0] = 0

    for i in range(n):
        for sum_v in range(max_v):

            # i 番目の品物を選ぶ場合
            if sum_v - val[i] >= 0:
                dp[i+1][sum_v] = min(dp[i][sum_v], dp[i][sum_v - val[i]] + wei[i])
            else:
                # i 番目の品物を選ばない場合
                dp[i+1][sum_v] = dp[i][sum_v]

    res = 0
    for i in range(100+10):
        for sum_v in range(max_v):
            if dp[i][sum_v] <= w and res < sum_v:
                res = sum_v

    print(res)

if __name__ == '__main__':
    main()