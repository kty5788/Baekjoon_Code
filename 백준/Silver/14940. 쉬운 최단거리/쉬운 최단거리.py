from collections import deque

n,m = map(int,input().split())
mapp = []
visited = [[False for i in range(m)] for j in range(n)]
for i in range(n):
    mapp.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(i,j):
    q = deque()
    q.append([i,j])

    visited[i][j] = True
    mapp[i][j] = 0

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and mapp[nx][ny] != 0:
                if not visited[nx][ny]:
                    q.append([nx,ny])
                    mapp[nx][ny] = mapp[x][y] + 1
                    visited[nx][ny] = True

    for i in range(n):
        for j in range(m):
            if mapp[i][j] == 1 and visited[i][j] == False:
                print(-1, end=' ')
            else:
                print(mapp[i][j], end=' ')
        print('')


for i in range(n):
    for j in range(m):
        if mapp[i][j] == 2:
            bfs(i,j)
            exit()