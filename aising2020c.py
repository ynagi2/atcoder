# sqrt(n)まででいいことに直前で気づいた
  # それまでは2次元累積和とかしてた
# y, zだけでなく，xもsqrt(n)とすればいいことに気づかなかった

import sys
input = sys.stdin.buffer.readline


import math

# def equation(a, b, c):
#     D = (b**2 - 4*a*c) ** (1/2)
#     x_1 = (-b + D) / (2 * a)
#     x_2 = (-b - D) / (2 * a)

#     return x_1, x_2



def main():
    n = int(input())

    ans = [0]*(n+1)

    for x in range(1, int(math.sqrt(n))):
        for y in range(1, int(math.sqrt(n))):
            for z in range(1, int(math.sqrt(n))):

                e = x**2 + y**2 + z**2 + x*y + y*z + z*x
                if e >= 1 and e <= n:
                    ans[int(e)] += 1

    for i in range(len(ans)-1):
        print(ans[i+1])




                # x_1, x_2 = equation(1, y+z, y**2 + y*z + z**2 - n)

                # if isinstance(x_1, float):
                #     x_1 = round(x_1, 5)
                #     if x_1.is_integer() == True and x_1 >= 1:
                #         cnt += 1

                # if isinstance(x_2, float):
                #     x_2 = round(x_2, 5)
                #     if x_2.is_integer() == True and x_2 >= 1:
                #         cnt += 1

        # print(cnt)




if __name__ == '__main__':
    main()
