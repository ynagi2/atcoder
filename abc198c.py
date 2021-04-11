import math
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

def main():
    r, x, y = map_int()
    dist = (x**2 + y**2) ** 0.5
    if dist >= r:
        print(math.ceil(dist / r))
    else:
        print(2)



if __name__ == '__main__':
    main()