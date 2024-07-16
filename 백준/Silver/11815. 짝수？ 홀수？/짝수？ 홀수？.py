import decimal
import math
n = int(input())
l = list(map(int,input().split()))

def cal(x):
    if (int(x**0.5))**2 == x:
        return 1
    else:
        return 0


for i in l:
    print(cal(i), end=' ')