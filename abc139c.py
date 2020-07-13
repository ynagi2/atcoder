def main():
    n = int(input())
    h = list(map(int, input().split()))

    score = []

    # next_jを入れる発想がなかった(そうするとO(N)なので間に合う)
    # 愚直にやるとTLE
    j = 0
    for i in range(n-1):
        if i != 0:
            j = next_j
        cnt = 0
        while True:
            if j >= n-1 or h[j] < h[j+1]:
                score.append(cnt)
                next_j = j+1
                break
            else:
                h[j] >= h[j+1]
                cnt += 1
                j += 1

    # これも入れ忘れていた
    if n == 1:
        print(0)
    else:
        print(max(score))

if __name__ == '__main__':
    main()