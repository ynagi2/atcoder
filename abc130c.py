
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

def main():
    w, h, x, y = map_int()
    if x == w / 2 and y == h / 2:
        print("{} {}".format(w*h/2, 1))
    else:
        print("{} {}".format(w*h/2, 0))



if __name__ == '__main__':
    main()