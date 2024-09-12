from collections import deque
N,M = map(int,input().split())
Map = [list(map(int,input().split())) for i in range(N)]
visited = [[False for i in range(M)] for j in range(N)]
zero_blank = []
two_virus = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

res = -1

def bfs(cnt=0):
    q = deque(two_virus)
    while q:
        x,y = q.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and Map[nx][ny] == 0:
                    q.append([nx,ny])
                    visited[nx][ny] = True
    
    for i in range(N):
        for j in range(M):
            if Map[i][j] == 0 and not visited[i][j]:
                cnt += 1

    return cnt
        
# 2의 좌표, 0의 좌표 찾기
for i in range(N):
    for j in range(M):
        if Map[i][j] == 2:
            two_virus.append([i,j])
        elif Map[i][j] == 0:
            zero_blank.append([i,j])


for i in zero_blank:
    for j in zero_blank:
        for k in zero_blank:
            if i != j and j != k and k != i:
                visited[i[0]][i[1]] = True
                visited[j[0]][j[1]] = True
                visited[k[0]][k[1]] = True
                Y = bfs()
                if Y > res:
                    res = Y
                visited = [[False for i in range(M)] for j in range(N)]

print(res)