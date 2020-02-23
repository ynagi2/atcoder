k = [int(input()) for i in range(4)]
p = 0

#どの硬貨も高々50枚
for a in range(k[0]+1):
    for b in range(k[1]+1):
        for c in range(k[2]+1):
            if 500*a + 100*b + 50*c == k[3]:
                p += 1

print(p)
