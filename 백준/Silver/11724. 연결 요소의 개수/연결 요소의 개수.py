import sys
sys.setrecursionlimit(100000)

n,m = map(int,input().split())
cnt = 0
graph = [[] for i in range(n+1)]
for i in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [None] + [False] * n

def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

while True:
    if False in visited:
        cnt += 1
        dfs(visited.index(False))
    else:
        break

print(cnt)