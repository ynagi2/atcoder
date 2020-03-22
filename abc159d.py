'''
def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result
'''

n = int(input())
a = list(map(int,input().split()))

num_count = {}

for e in a:
    if e in num_count.keys():
        num_count[e] += 1
    else:
        num_count[e] = 1

s = 0
c = set()

for i in range(n):
    if a[i] not in c:
        num = num_count[a[i]]
        s += num*(num-1) / 2
        c.add(a[i])

for i in range(n):
    print(int(s - (num_count[a[i]] - 1) ))



'''
Aと同様，r=2と決まっているのでcombination使う必要ない
全パターンからk番目の数について，kが絡む組み合わせを引けばよかった

.count使おうとするとそれだけで時間がかかる
→各数値の出現回数を辞書にしておく
'''