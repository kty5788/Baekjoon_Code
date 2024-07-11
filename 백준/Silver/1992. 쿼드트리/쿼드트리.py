n = int(input())
video = []
for i in range(n):
    video.append([])
    m = list(input())
    for j in m:
        video[-1].append(j)

def divide_conquer(x,y,size):
    is_same = video[x][y]
    for i in range(x,x+size):
        for j in range(y,y+size):
            if is_same != video[i][j]:
                is_same = False
    
    if is_same:
        #print(video[x][y],x,y)
        print(f'{is_same}',end='')
    else:
        print('(',end='')
        divide_conquer(x,y,size//2)
        divide_conquer(x,y+size//2,size//2)
        divide_conquer(x+size//2,y,size//2)
        divide_conquer(x+size//2,y+size//2,size//2)
        print(')',end='')

divide_conquer(0,0,n)