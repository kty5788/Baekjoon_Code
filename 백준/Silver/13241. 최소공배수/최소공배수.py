a,b = map(int,input().split())
if b > a:
    a,b = b,a
f = a*b
while b != 0:
    if a%b == 0:
        break
    else:
        a,b = b,a%b
print(int(f/b))