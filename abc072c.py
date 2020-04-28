from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))

dic = defaultdict(int)
for elem in a:
    dic[elem] += 1
    dic[elem - 1] += 1
    dic[elem + 1] += 1

#max valueを出力
print(max(dic.values()))