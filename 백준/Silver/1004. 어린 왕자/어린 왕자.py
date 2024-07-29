t = int(input())
for i in range(t):
    cnt = 0
    x1,y1,x2,y2 = map(int,input().split())
    n = int(input())
    for j in range(n):
        cx,cy,r = map(int,input().split())
        if ((cx-x1)**2 + (cy-y1)**2) < r**2 and (cx-x2)**2 + (cy-y2)**2 > r**2:
            cnt += 1
        elif (cx-x2)**2 + (cy-y2)**2 < r**2 and (cx-x1)**2 + (cy-y1)**2 > r**2:
            cnt += 1
    print(cnt)