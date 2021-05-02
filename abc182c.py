
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))
# mod = 10**9 + 7

# 単純に3の剰余系に沿って数字を消してもできる
def main():
    n = input()
    for i in range(2**len(n)-1):
        string = str(bin(2**len(n)-(i+1))[2:])
        if len(string) < len(n):
            string = '0'*(len(n) - len(string)) + string
        tf = []
        for z in range(len(n)):
            tf.append(int(string[z]))
        new_n = ""
        k = 0
        for j in range(len(n)):
            if tf[j] == 1:
                new_n += n[j]
            else:
                k += 1
        if int(new_n) % 3 == 0:
            print(k)
            exit()
    print(-1)



if __name__ == '__main__':
    main()