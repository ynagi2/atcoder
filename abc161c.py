n, k = map(int,input().split())
# print(min(abs(n - k * int(n/k)), abs(n - k * (int(n/k) + 1))))

# もっと簡単に書けばこうか でもなぜ上は通らない？
print(min(n%k, k-(n%k)))