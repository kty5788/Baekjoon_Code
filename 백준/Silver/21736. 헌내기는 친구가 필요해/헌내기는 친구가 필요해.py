import sys
input = sys.stdin.readline

N,M = map(int,input().split())
campus = [list(input()) for i in range(N)]
visited = [[False for row in range(M)] for col in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(i,j,cnt=0):
    stack = []
    stack.append([i,j])
    visited[i][j] = True
    
    while stack:
        x,y = stack.pop()

        if campus[x][y] == 'P':
            cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and campus[nx][ny] != 'X':
                    stack.append([nx,ny])
                    visited[nx][ny] = True

    return cnt

for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            res = dfs(i,j)
            if res == 0:
                print('TT')
            else:
                print(res)
            exit()