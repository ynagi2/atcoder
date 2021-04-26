
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))
# mod = 10**9 + 7

def main():
    s = input()
    cnt = 0
    for i in range(len(s)//2):
        if s[i] != s[-1*(i+1)]:
            cnt += 1
    print(cnt)



if __name__ == '__main__':
    main()