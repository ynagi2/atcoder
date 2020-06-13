n, a, b = map(int,input().split())
count = 0

for i in range(1, n+1):
    temp = list(str(i))
    val = 0
    for j in temp:
        val += int(j)

    if val >= a and val <= b:
        count += i

print(count)