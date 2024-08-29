import sys
input = sys.stdin.readline

n = int(input())
color = [list(input()) for i in range(n)]
cnt = 0
visited = [[False for row in range(n)] for col in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# dfs stack으로 구현
def dfs(i,j,color_blind=False):
    stack = []
    stack.append([i,j])
    color_rgb = color[i][j]
    visited[i][j] = True
    
    while stack:
        x,y = stack.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if color_blind and color_rgb != 'B':
                    if not visited[nx][ny] and color[nx][ny] != 'B':
                        stack.append([nx,ny])
                        visited[nx][ny] = True
                else:
                    if not visited[nx][ny] and color[nx][ny] == color_rgb:
                        stack.append([nx,ny])
                        visited[nx][ny] = True
                    
# 적록색약이 아닌 사람
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j,color_blind=False)
            cnt += 1

print(cnt)

cnt = 0
visited = [[False for row in range(n)] for col in range(n)]

# 적록색약인 사람
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j,color_blind= True)
            cnt += 1

print(cnt)