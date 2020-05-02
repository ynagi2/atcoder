abc = list(map(int,input().split()))

count = 0
abc.sort(reverse=True)

# 偶奇が一致
if abc[0] % 2 == abc[1] % 2 and abc[0] % 2 == abc[2] % 2:
    count += (abc[0] - abc[1]) / 2
    count += (abc[0] - abc[2]) / 2

# 偶奇が両方違う
elif abc[0] % 2 != abc[1] % 2 and abc[0] % 2 != abc[2] % 2:
    abc[1] += 1
    abc[2] += 1
    count += 1

    count += (abc[0] - abc[1]) / 2
    count += (abc[0] - abc[2]) / 2

# 偶奇が片方違う
else:
    if abc[0] % 2 == abc[1] % 2:
        abc[0] += 1
        abc[1] += 1
        count += 1

        count += (abc[0] - abc[1]) / 2
        count += (abc[0] - abc[2]) / 2

    else:
        abc[0] += 1
        abc[2] += 1
        count += 1

        count += (abc[0] - abc[1]) / 2
        count += (abc[0] - abc[2]) / 2

print(int(count))