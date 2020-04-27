HW = list(map(int,input().split()))
s = [input() for i in range(HW[0])]


# #が上下左右.に囲まれていたらNo
for j in range(len(s) - 1):
    for i in range(len(s[j]) - 1):
        if s[j][i] == "#" and s[j][i] != s[j][i+1] and (s[j][i] != s[j][i-1] or i == 0):
            if s[j][i] != s[j+1][i] and (s[j][i] != s[j-1][i] or j == 0):
                print("No")
                exit()

print("Yes")