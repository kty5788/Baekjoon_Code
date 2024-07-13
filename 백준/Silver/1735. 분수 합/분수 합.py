import math
x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())

def lcm(a,b):
    return int(a*b/math.gcd(y1,y2))

denominator = lcm(y1,y2)
numerator = int(x1*(denominator/y1)) + int(x2*(denominator/y2))

gcd = math.gcd(denominator,numerator)
print(int(numerator/gcd),int(denominator/gcd))