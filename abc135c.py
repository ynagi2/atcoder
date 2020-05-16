n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

num = 0
for i in range(n):
    if b[n-1-i] > a[n-i]:
        num += a[n-i]
        temp = b[n-1-i] - a[n-i]
        if temp <= a[n-i-1]:
            a[n-i-1] -= temp
            num += temp
        else:
            num += a[n-i-1]
            a[n-i-1] = 0
    else:
        a[n-i] -= b[n-1-i]
        num += b[n-1-i]
    
print(num)