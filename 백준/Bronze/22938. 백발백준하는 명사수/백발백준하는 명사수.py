x1,y1,r1 = list(map(int,input().split()))
x2,y2,r2 = list(map(int,input().split()))

length = ((x1-x2)**2 + (y1-y2)**2)**0.5
if length < r1 + r2:
    print('YES')
else:
    print('NO')