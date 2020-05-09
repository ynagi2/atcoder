# 整数問題では，とりあえず一通り紙に列挙してパターンを探す
# 7%5 = 2, 14%5 = 4, ... としていくと，余りには周期性がある
# 入力はなんでもよいこともわかる(とりあえずその倍数とだけ考えればいい)
# この例なら，7k(k=1~5)を5で割ったときの余りがCと一致するやつがあるか考えればいい
a, b, c = map(int,input().split())

for i in range(b):
    if (a * (i+1)) % b == c:
        print("YES")
        exit()

print("NO")