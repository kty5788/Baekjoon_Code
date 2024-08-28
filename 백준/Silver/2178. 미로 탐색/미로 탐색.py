from collections import deque
N,M = map(int,input().split())
maze = [list(input()) for i in range(N)]
visited = [[False for row in range(M)] for col in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    q = deque([[0,0]])
    maze[0][0] = 1
    visited[0][0] = True

    while q:
        row,col = q.popleft()
        for i in range(4):
            nx = row + dx[i]
            ny = col + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and maze[nx][ny] != '0':
                    maze[nx][ny] = maze[row][col] + 1
                    q.append([nx,ny])
                    visited[nx][ny] = True

bfs()
print(maze[N-1][M-1])