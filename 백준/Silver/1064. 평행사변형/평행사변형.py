x1,y1,x2,y2,x3,y3 = list(map(int,input().split()))

if (x1 == x2 == x3) or (y1 == y2 == y3):
    print(-1.0)
elif (y3-y2)*(x2-x1) == (y2-y1)*(x3-x2):
    print(-1.0)
else:
    d1 = ((x1-x2)**2 + (y1-y2)**2)**0.5
    d2 = ((x2-x3)**2 + (y2-y3)**2)**0.5
    d3 = ((x3-x1)**2 + (y3-y1)**2)**0.5
    l = [(d1*2 + d2 *2), (d1*2 + d3*2), (d2*2 + d3*2)]
    ans = max(l) - min(l)
    print(f'{ans:.15f}')