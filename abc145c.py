from itertools import permutations

def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

def dist(i, j, x, y):
    return ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5

def main():
    n = int(input())
    x, y = [], []
    for i in range(n):
        a, b = map_int()
        x.append(a)
        y.append(b)
    towns = [i for i in range(n)]
    p = list(permutations(towns))
    a_len = []
    for e in p:
        tmp = 0
        for i in range(len(e)-1):
            tmp += dist(e[i], e[i+1], x, y)
        a_len.append(tmp)
    print(sum(a_len)/len(a_len))


if __name__ == '__main__':
    main()