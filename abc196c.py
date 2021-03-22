
# 単に1, 1000001でloop回せばシンプルだった
def main():
    n = int(input())
    keta = len(str(n))

    dic = {}
    for j in range(6):
        dic[j] = [i+1*(10**j) for i in range(9*(10**j))]

    cnt = 0
    for i in range(keta//2):
        for e in dic[i]:
            comp = str(e) + str(e)
            if int(comp) <= n:
                cnt += 1
            else:
                print(cnt)
                exit()
    print(cnt)



if __name__ == '__main__':
    main()