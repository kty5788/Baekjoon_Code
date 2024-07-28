import sys
input = sys.stdin.readline

w,h,x,y,p = map(int,input().split())
radius = h/2
cnt = 0
for i in range(p):
    p_x,p_y = map(int,input().split())
    if p_x >= x and p_x <= x+w and p_y >= y and p_y <= y+h:
        cnt += 1
    else:
        if (p_x-x)**2 + (p_y-(y+radius))**2 <= radius**2:
            cnt += 1
        elif (p_x-(x+w))**2 + (p_y-(y+radius))**2 <= radius**2:
            cnt += 1

print(cnt)