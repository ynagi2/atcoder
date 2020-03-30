import collections
n, k = map(int,input().split())
a = list(map(int,input().split()))

num = collections.defaultdict(int)

for elem in a:
    num[elem] += 1

count = 0
if len(num) <= k:
    print(count)
else:
    # sort使う発想なかった(出現頻度の昇順にソート)
    sorted_num = sorted(num.items(), key=lambda x:x[1])
    # 減らさなければいけない種類数だけ繰り返す
    for i in range(len(num) - k):
        # 出現頻度の少ない数から順に，その頻度を加えていく
	    count += sorted_num[i][1]

    print(count)

