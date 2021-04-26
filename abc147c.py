
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))
# mod = 10**9 + 7

def main():
    n = int(input())
    x, y = {}, {}
    for i in range(n):
        a = int(input())
        u, v = [], []
        for j in range(a):
            s, t = map_int()
            u.append(s)
            v.append(t)
        x[i+1] = u
        y[i+1] = v
    
    for i in range(2**n):
        string = str(bin(2**n-(i+1))[2:])
        if len(string) < n:
            string = '0'*(n - len(string)) + string
        tf = []
        for z in range(n):
            tf.append(int(string[z]))
        f = True
        for j in range(n):
            if tf[j] == 0:
                continue
            for k in range(len(x[j+1])):
                if tf[x[j+1][k]-1] != y[j+1][k]:
                    f = False
        if f:
            cnt = 0
            for e in tf:
                if e == 1:
                    cnt += 1
            print(cnt)
            break


if __name__ == '__main__':
    main()