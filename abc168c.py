import math
a, b, h, m = map(int,input().split())

at = (m + h*60) * 0.5
bt = m * 6

theta = abs(at - bt)
if theta > 180:
    theta = 360 - theta

c2 = a**2 + b**2 - 2*a*b*math.cos(math.radians(theta))

print(c2**(1/2))