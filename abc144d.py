import math

def main():
    a, b, x = map(int, input().split())
    # こっちの図示をミスった
    # 水が溢れるなら対辺はbでしょ
    if x <= a*a*b/2:
        ans = a*b*b/(2*x)
        print(math.degrees(math.atan(ans)))
    else:
        ans = (2*a*b*a - 2*x) / (a**3)
        print(math.degrees(math.atan(ans)))

if __name__ == '__main__':
    main()