
def main():
    s = input()
    a, b, c, d = map(int, input().split())
    print(s[:a] + "\"" + s[a:b] + "\"" + s[b:c] + "\"" + s[c:d] + "\"" + s[d:])



if __name__ == '__main__':
    main()