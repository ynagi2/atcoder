import math

num = list(map(int,input().split()))

'''
誤差でアウト

a = num[0]**0.5
b = num[1]**0.5
c = num[2]**0.5

if math.sqrt(num[0]) + math.sqrt(num[1]) < math.sqrt(num[2]):
    print("Yes")
else:
    print("No")

誤差を小さくするテクニックらしいが，これでもダメだった
if (c**2 - (a+b)**2)/(c+a+b) > 0:
    print("Yes")
else:
    print("No")
'''


#両辺2乗する発想はあったが，2回2乗するところまで考えが及ばなかった
a = num[0]
b = num[1]
c = num[2]

if (c-(a+b))**2 - 4*a*b > 0 and c-a-b > 0:
    print("Yes")
else:
    print("No")