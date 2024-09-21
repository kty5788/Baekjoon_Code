n = int(input())
l = [list(map(int,input().split())) for i in range(n)]
visited = [[False for i in range(n)] for i in range(n)]
graph = [[] for i in range(n)]

for i in range(n):
    for j in range(n):
        if l[i][j] == 1:
            graph[i].append(j)
            visited[i][j] = True

def dfs(start,end):
    stack = [start]
    while stack:
        
        x = stack.pop()
        for i in graph[x]:
            if i == end:
                return 1
            else:
                if not visited[x][i]:
                    stack.append(i)
                    visited[x][i] = True
    return 0

for i in range(n):
    for j in range(n):
        visited = [[False for i in range(n)] for i in range(n)]
        print(dfs(i,j), end=' ')
    print('')