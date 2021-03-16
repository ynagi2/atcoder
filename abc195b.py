import math

def main():
    a, b, w = map(int, input().split())
    w = 1000 * w

    m1 = math.floor(w / a)
    m2 = math.ceil(w / b)

    if a * m2 > w:
        print("UNSATISFIABLE")
        exit()
    
    print("{} {}".format(m2, m1))

    


if __name__ == '__main__':
    main()