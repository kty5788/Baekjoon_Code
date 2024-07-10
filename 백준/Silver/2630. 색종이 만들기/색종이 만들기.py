n = int(input())
colored_paper = []
cnt = [0,0]
for i in range(n):
    colored_paper.append(list(input().split()))

def divide_conquer(x,y,size):
    is_same = colored_paper[x][y]
    for i in range(x,x+size):
        for j in range(y,y+size):
            if is_same != colored_paper[i][j]:
                is_same = False

    if not is_same:
        divide_conquer(x,y,size//2)
        divide_conquer(x+size//2,y,size//2)
        divide_conquer(x,y+size//2,size//2)
        divide_conquer(x+size//2,y+size//2,size//2)

    else:
        if is_same == '0':
            cnt[0] += 1
        else:
            cnt[1] += 1
    return

divide_conquer(0,0,n)
print(*cnt,sep='\n')