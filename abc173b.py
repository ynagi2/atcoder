# 以下は確かに速いが，文字列の場合にはstripやdecodeが必要になる
# import sys
# input = sys.stdin.buffer.readline

def main():
    n = int(input())
    s = [input() for i in range(n)]

    ac = 0
    wa = 0
    tle = 0
    re = 0

    for e in s:
        if e == "AC":
            ac += 1
        elif e == "WA":
            wa += 1
        elif e == "TLE":
            tle += 1
        else:
            re += 1

    # for i in range(len(s)):
    #     if s[i].strip().decode() == "AC":
    #         ac += 1
    #     elif s[i].strip().decode() == "WA":
    #         wa += 1
    #     elif s[i].strip().decode() == "TLE":
    #         tle += 1
    #     else:
    #         re += 1

    print("AC x {}".format(str(ac)))
    print("WA x {}".format(str(wa)))
    print("TLE x {}".format(str(tle)))
    print("RE x {}".format(str(re)))

if __name__ == '__main__':
    main()