
def main():
    s = input()
    k = int(input())

    cnt = 0
    for e in s:
        if int(e) == 1:
            cnt += 1
            if cnt == k:
                print(e)
                break
            else:
                continue
        print(e)
        break

if __name__ == '__main__':
    main()