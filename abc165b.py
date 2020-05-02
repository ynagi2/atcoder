x = int(input())

y = 100
i = 0

while True:
    if y >= x:
        break
    y = int(y * 1.01)
    i += 1

print(i)