import sys
import math
input = sys.stdin.readline

a,b,h = map(int,input().split())

if a > b:
    a,b=b,a

if a != b:
    lost_h = (a*h)/(b-a)
    print(round(((b**2+(lost_h+h)**2)-(a**2+lost_h**2))*math.pi,7))
else:
    print(-1)