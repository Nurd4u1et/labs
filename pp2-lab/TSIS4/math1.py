import math
def degtorad(deg):
    rad = deg * math.pi / 180
    return rad
deg = int(input())
radian = degtorad(deg)
print(radian)