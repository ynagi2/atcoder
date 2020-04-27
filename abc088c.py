c1 = list(map(int,input().split()))
c2 = list(map(int,input().split()))
c3 = list(map(int,input().split()))

a2_a1 = c2[0] - c1[0]
a3_a2 = c3[0] - c2[0]
a1_a3 = c1[0] - c3[0]

b2_b1 = c1[1] - c1[0]
b3_b2 = c1[2] - c1[1]
b1_b3 = c1[0] - c1[2]

if a2_a1 != c2[1] - c1[1] or a2_a1 != c2[2] - c1[2]:
    print("No")
elif a3_a2 != c3[1] - c2[1] or a3_a2 != c3[2] - c2[2]:
    print("No")
elif a1_a3 != c1[1] - c3[1] or a1_a3 != c1[2] - c3[2]:
    print("No")
elif b2_b1 != c2[1] - c2[0] or b2_b1 != c3[1] - c3[0]:
    print("No")
elif b3_b2 != c2[2] - c2[1] or b3_b2 != c3[2] - c3[1]:
    print("No")
elif b1_b3 != c2[0] - c2[2] or b1_b3 != c3[0] - c3[2]:
    print("No")
else:
    print("Yes")