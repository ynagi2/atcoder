
def main():
    s = input()
    ans = s[0] + str(len(s) - 2) + s[-1]
    print(ans)


if __name__ == '__main__':
    main()