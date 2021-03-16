
def main():
    n = int(input())

    arr = [3, 6, 9, 12, 15]
    if len(str(n)) == 16:
        print((10**6 - 10**3)*1 + (10**9 - 10**6)*2 + (10**12 - 10**9)*3 + (10**15 - 10**12)*4 + 5)
        exit()

    for i, e in enumerate(arr):
        if len(str(n)) <= e:
            p = i
            break
    if p == 0:
        print(0)
        exit()
    c = 0
    for i in range(p):
        if i != p-1:
            c += (10**(3*(i+2)) - 10**(3*(i+1)))*(i+1)
        else:
            c += p*((n - 10**(3*p)) + 1)
    print(c)



if __name__ == '__main__':
    main()