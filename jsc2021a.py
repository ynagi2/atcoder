
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

def main():
    x, y, z = map_int()
    i = 1
    while True:
        if y / x <= i / z:
            break
        else:
            i += 1
    print(i-1)




if __name__ == '__main__':
    main()