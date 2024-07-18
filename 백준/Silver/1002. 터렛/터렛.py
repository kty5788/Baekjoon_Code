n = int(input())
for i in range(n):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    distance = ((x2-x1)**2 + (y2-y1)**2)
    if (x1,y1) == (x2,y2):
        if r1 != r2:
            print(0)
        else:
            print(-1)
    else:
        if distance < (r1+r2)**2 and ((r2-r1)**2 < distance < (r1+r2)**2):
            print(2)
        elif distance == (r1+r2)**2 or (r1-r2)**2 == distance:
            print(1)
        else:
            print(0)