n = int(input())
a = list(map(int,input().split()))

divide = 0
i = 0

while i < n:
    while i+1 < n and a[i] == a[i+1]:
        i += 1

    if i+1 < n and a[i] < a[i+1]:
        while i+1 < n and a[i] <= a[i+1]:
            i += 1

    elif i+1 < n and a[i] > a[i+1]:
        while i+1 < n and a[i] >= a[i+1]:
            i += 1

    divide += 1
    i += 1

print(divide)


# 入力例2みたいなとき，ひとかたまりに最低2個数字が入るはずなのに，これでは1つしかいれられない
# やろうとしていることは間違っていない(iとelem_countがあって複雑)
# elem_count = 0
# divide = 0

# while elem_count < len(a) - 1:
#     pm = a[elem_count+1] - a[elem_count]

#     if pm > 0 and elem_count < len(a) - 2:
#         for i in range(elem_count, len(a) - 2):
#             elem_count += 1
#             if a[i+2] < a[i+1] or elem_count >= len(a) - 1:
#                 divide += 1
#                 break

#     elif pm < 0 and elem_count < len(a) - 2:
#         for i in range(elem_count, len(a) - 2):
#             elem_count += 1
#             if a[i+2] > a[i+1] or elem_count >= len(a) - 1:
#                 divide += 1
#                 break
    
#     else:
#         elem_count += 1

# print(divide)