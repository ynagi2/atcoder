import sys
input = sys.stdin.buffer.readline
import itertools

def to_str(string, array):
    for i in array:
        string += str(i)
    return string

def main():
    n = int(input())
    p = list(map(int,input().split()))
    q = list(map(int,input().split()))

    p_str = ""
    q_str = ""
    p_str = to_str(p_str, p)
    q_str = to_str(q_str, q)
    
    arr = [i+1 for i in range(n)]

    nums = list(itertools.permutations(arr))
    nums_str = []
    for e in nums:
        temp = ""
        temp = to_str(temp, e)
        nums_str.append(temp)

    nums_str.sort()

    a = nums_str.index(p_str) + 1
    b = nums_str.index(q_str) + 1
    print(abs(a-b))

if __name__ == '__main__':
    main()