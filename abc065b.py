n = int(input())
a = [int(input()) for _ in range(n)]

i = 0
count = 0

# 2回通ったらループしているはず
root = set()
while True:
    light = a[i]
    count += 1

    if i not in root:
        root.add(i)
    else:
        print(-1)
        break

    if light == 2:
        print(count)
        break

    i = light - 1