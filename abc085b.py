n = input()
d = [int(input()) for i in range(int(n))]

d.sort(reverse=True)

#重複する数値ペアの数をカウントして，nから引けばいい
dupe = 0
for i in range(len(d)-1):
    if d[i] == d[i+1]:
        dupe += 1

print(int(n)-dupe)