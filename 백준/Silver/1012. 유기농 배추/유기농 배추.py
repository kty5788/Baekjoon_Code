import sys 
sys.setrecursionlimit(10000) 

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < m):
            if graph[nx][ny]:
                graph[nx][ny] = 0
                dfs(nx,ny)


n = int(input())
for i in range(n):
    cnt = 0
    m,n,k = map(int,input().split())
    graph = [[0 for row in range(m)] for col in range(n)]
    for j in range(k):
        x,y = map(int,input().split())
        graph[y][x] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i,j)
                cnt += 1
    print(cnt)
