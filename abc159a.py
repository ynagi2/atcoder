import itertools
a = list(map(int,input().split()))

s = [i for i in range(a[0])]
t = [i for i in range(a[1])]

n = list(itertools.combinations(s, 2))
m = list(itertools.combinations(t, 2))

print(len(n) + len(m))

'''
わざわざこんなの描いてしまったが，nCr のrは2で固定なのだから，
n*(n-1)/2 + m*(m-1)/2 でよかったじゃんあほ
'''
