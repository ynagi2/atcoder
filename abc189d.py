
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

def main():
    n = int(input())
    s = []
    for _ in range(n):
        tmp = input()
        s.append(tmp)
    ans = 1
    for i in range(len(s)):
        if s[i] == "OR":
            ans += 2**(i+1)
    print(ans)

if __name__ == '__main__':
    main()