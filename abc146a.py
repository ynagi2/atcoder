
def map_str(): return map(input().split())
def map_int(): return map(int, input().split())
def lmap_int(): return list(map(int, input().split()))
def lmap_str(): return list(map(input().split()))

def main():
    s = input()
    arr = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    if s == "SUN":
        print(7)
    else:
        print(6 - arr.index(s))



if __name__ == '__main__':
    main()