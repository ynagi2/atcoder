
def main():
    n = int(input())
    s = input()

    cnt = 1
    for i in range(len(s)):
        if i == 0:
            continue
        if s[i] != s[i-1]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()