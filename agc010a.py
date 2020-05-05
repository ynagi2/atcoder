n = int(input())
a = list(map(int,input().split()))

# これってつまり，aの要素の合計が偶数 or not で判定すればいい

count = 0
for i in a:
    if i % 2 != 0:
        count += 1

if count % 2 != 0:
    print("NO")
else:
    print("YES")

