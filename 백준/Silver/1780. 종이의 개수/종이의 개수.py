n = int(input())
paper = []
ans = [0,0,0]
for i in range(n):
    paper.append(list(input().split()))

def divide_conquer(x,y,size):
    is_same = paper[x][y]
    for i in range(x,x+size):
        for j in range(y,y+size):
            if is_same != paper[i][j]:
                is_same = False
    
    if is_same:
        ans[int(is_same)+1] += 1
    else:
        divide_conquer(x,y,size//3)
        divide_conquer(x+size//3,y,size//3)
        divide_conquer(x+size//3*2,y,size//3)
        divide_conquer(x,y+size//3,size//3)
        divide_conquer(x+size//3,y+size//3,size//3)
        divide_conquer(x+size//3*2,y+size//3,size//3)
        divide_conquer(x,y+size//3*2,size//3)
        divide_conquer(x+size//3,y+size//3*2,size//3)
        divide_conquer(x+size//3*2,y+size//3*2,size//3)

divide_conquer(0,0,n)
print(*ans,sep='\n')