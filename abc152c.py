n = int(input())
p = list(map(int,input().split()))

count = 0
p_min = p[0]

for elem in p:
    # いちいち最小値を探すのは時間がかかる
    # その都度最小値を更新していく
    if elem <= p_min:
        count += 1
        p_min = elem

print(count)
