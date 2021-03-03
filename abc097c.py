
def main():
    s = input()
    k = int(input())
    subset = set()
    # kまで回せば十分じゃん
    # これでTLEでも200点はもらえる
    for i in range(k):
        arr = []
        for j in range(len(s) - i):
            arr.append(s[j:j+i+1])
        arr.sort()
        for h in range(min(k, len(arr))):
            subset.add(arr[h])
    l = list(subset)
    l.sort()
    print(l[k-1])

if __name__ == '__main__':
    main()