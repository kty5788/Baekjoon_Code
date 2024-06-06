t = int(input())
for i in range(t):
    x1,y1,x2,y2,x3,y3,x4,y4 = list(map(int,input().split()))
    original_area = (x2-x1) * (y2-y1)
    if x3 >= x2 or x4 <= x1:
        behind_x = 0
    else:
        behind_x = min(x2,x4) - max(x1,x3)
    
    if y3 >= y2 or y4 <= y1:
        behind_y = 0
    else:
        behind_y = min(y2,y4) - max(y1,y3)
    
    behind_area = behind_x * behind_y
    if original_area - behind_area < 0:
        print(0)
    else:
        print(original_area - behind_area)