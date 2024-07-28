def dfs(i,j):
    if graph[i][j] == '-':
        graph[i][j] = 0
        if j != m-1 and graph[i][j+1] == '-':
            dfs(i,j+1)
    elif graph[i][j] == '|':
        graph[i][j] = 0
        if i != n-1 and graph[i+1][j] == '|':
            dfs(i+1,j)
    
    return

n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(input()))


cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '-' or graph[i][j] == '|':
            dfs(i,j)
            cnt += 1

print(cnt)