x = int(input())

u1 = int(x / 500)
u2 = int((x - u1*500) / 5)

print(u1*1000 + u2*5)