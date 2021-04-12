from itertools import permutations

def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

# 計算量含め方針はあっていたが，計算がわずかに間に合わなかった
def main():
    s1 = list(input())
    s2 = list(input())
    s3 = list(input())
    alp = set(s1 + s2 + s3)
    if len(alp) > 10:
        print("UNSOLVABLE")
        exit()
    alp = list(alp)
    t = [i for i in range(10)]
    # permutationのlistを作る必要はない
    for p in permutations(t, len(alp)):
        dic = {}
        for i, e in enumerate(alp):
            dic[e] = p[i]
        n1, n2, n3 = "", "", ""
        for e in s1:
            n1 += str(dic[e])
        for e in s2:
            n2 += str(dic[e])
        for e in s3:
            n3 += str(dic[e])
        # intとstringの変換は少し時間がかかるらしい
        in1, in2, in3 = int(n1), int(n2), int(n3)
        if in1 + in2 == in3 and in1 != 0 and in2 != 0 and in3 != 0 and len(str(in1)) == len(s1) and len(str(in2)) == len(s2) and len(str(in3)) == len(s3):
            print(n1)
            print(n2)
            print(n3)
            exit()
    print("UNSOLVABLE")


if __name__ == '__main__':
    main()