a, b, c, d = map(int,input().split())

# 単にif min(b, d) >= max(a, c): min(b, d) - max(a, c) else 0でいいじゃん
# めっちゃ集中力切れてた

if min(b, d) >= max(a, c):
    print(min(b, d) - max(a, c))
else:
    print(0)

# # 2次関数の最大値を求める感じの場合分け(普通にWAしたウケる)
# if a >= d or b <= c:
#     print(0)
#     exit()

# # bの位置にも注目する必要があるので面倒
# if d <= b and d >= a and c <= a:
#     print(d-a)
#     exit()

# if c >= a and b >= d:
#     print(d-c)
#     exit()

# if d >= b and c <= b:
#     print(b-c)
#     exit()

# if a >= c and d >= b:
#     print(b-a)
#     exit()