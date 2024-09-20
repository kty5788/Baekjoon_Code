from collections import deque

m,n,h = map(int,input().split())
arr = [[list(map(int,input().split())) for i in range(n)] for i in range(h)]
visited = [[[False for i in range(m)] for j in range(n)] for k in range(h)]

q = deque()

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]


for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                q.append([i,j,k])
                visited[i][j][k] = True

def bfs():
    while q:
        x,y,z = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if not visited[nx][ny][nz] and arr[nx][ny][nz] != -1:
                    arr[nx][ny][nz] = arr[x][y][z] + 1
                    visited[nx][ny][nz] = True
                    q.append([nx,ny,nz])

bfs()

ans = -1
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:
                print(-1)
                exit()
            else:
                if arr[i][j][k] > ans:
                    ans = arr[i][j][k]

print(ans-1)