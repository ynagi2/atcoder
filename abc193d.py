from collections import defaultdict

def main():
    k = int(input())
    s = input()
    t = input()

    taka = defaultdict(int)
    ao = defaultdict(int)
    rest = [k]*9

    for i in range(4):
        taka[int(s[i])] += 1
        rest[int(s[i]) - 1] -= 1
        ao[int(t[i])] += 1
        rest[int(t[i]) - 1] -= 1
    win = set()
    sum_rest = sum(rest)
    for i in range(9):
        if rest[i] == 0:
            continue
        for j in range(9):
            if i == j and rest[j] == 1 or rest[j] == 0:
                continue
            taka[i+1] += 1
            ao[j+1] += 1
            t = 0
            a = 0
            for k, v in taka.items():
                t += k * (10 ** v)
            for k, v in ao.items():
                a += k * (10 ** v)
            if t > a:
                win.add((i+1, j+1))
            taka[i+1] -= 1
            ao[j+1] -= 1
    for i in range(9):
        if rest[i] == 0:
            continue
        for j in range(9):
            if i == j and rest[j] == 1 or rest[j] == 0:
                continue
            ao[i+1] += 1
            taka[j+1] += 1
            t = 0
            a = 0
            for k, v in ao.items():
                a += k * (10 ** v)
            for k, v in taka.items():
                t += k * (10 ** v)
            if t > a:
                win.add((j+1, i+1))
            ao[i+1] -= 1
            taka[j+1] -= 1
    prob = 0
    for e in win:
        if e[0] != e[1]:
            prob += (rest[e[0]-1] / sum_rest) * (rest[e[1]-1] / (sum_rest - 1))
        else:
            prob += (rest[e[0]-1] / sum_rest) * ((rest[e[1]-1] - 1) / (sum_rest - 1))
    print(prob)


if __name__ == '__main__':
    main()