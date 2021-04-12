
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

def main():
    n = int(input())
    w = []
    say = []
    for _ in range(n):
        tmp = input()
        w.append(tmp)
    for i in range(n):
        if i != 0 and w[i-1][-1] != w[i][0]:
            print("No")
            exit()
        if w[i] in say:
            print("No")
            exit()
        say.append(w[i])
    print("Yes")




if __name__ == '__main__':
    main()