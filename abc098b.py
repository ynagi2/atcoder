n = int(input())
s = input()

num = 0
for i in range(n-1):
    x = s[:i+1]
    y = s[i+1:]

    setx = {i for i in x}
    sety = {i for i in y}
    common = setx & sety

    num = max(num, len(common))

print(num)