n, k = map(int,input().split())
p = list(map(int,input().split()))

cumsum = [0]*(n+1)
for i in range(n):
    cumsum[i+1] = cumsum[i] + p[i]

maxe = 0
idx = 0
for i in range(n-k+1):
    if cumsum[i+k] - cumsum[i] > maxe:
        maxe = cumsum[i+k] - cumsum[i]
        idx = i

# p_iを引数，期待値を返り値
def ex(n):
    return 0.5 * n + 0.5

res = 0
for i in range(k):
    res += ex(p[i+idx])

print(res)