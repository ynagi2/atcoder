# 重複を削除する処理を別で行うと1TLE
# 最初のforの中で削除も済ませてしまう発想がなかった
def main():
    s = input()
    t = ""
    f = False
    for e in s:
        if e == "R" and not(f):
            f = True
        elif e == "R" and f:
            f = False
        else:
            if f:
                if t == "":
                    t = e + t
                    continue
                if e == t[0]:
                    t = t[1:]
                else:
                    t = e + t
            else:
                if t == "":
                    t = t + e
                    continue
                if e == t[-1]:
                    t = t[:-1]
                else:
                    t = t + e
    if f:
        print(t[::-1])
    else:
        print(t)
    
    


if __name__ == '__main__':
    main()