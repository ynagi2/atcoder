n = int(input())
location = [[0]*3]*n

for i in range(n):
    location[i] = list(map(int,input().split()))

# print(location) -> [[3, 1, 2], [6, 1, 1]]
# 合計値と同じ奇数or偶数になっていればいい
# x+y <= t も必要
for i in range(n):
    if location[i][1] + location[i][2] > location[i][0]:
        print("No")
        flag = False
        break
    elif location[i][0] % 2 != (location[i][1] + location[i][2]) % 2:
        print("No")
        flag = False
        break
    else:
        flag = True

if flag:
    print("Yes")