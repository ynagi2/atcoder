ABCD = list(map(int,input().split()))

while True:
    ABCD[2] = ABCD[2] - ABCD[1]
    if ABCD[2] <= 0:
        print("Yes")
        break

    ABCD[0] = ABCD[0] - ABCD[3]
    if ABCD[0] <= 0:
        print("No")
        break