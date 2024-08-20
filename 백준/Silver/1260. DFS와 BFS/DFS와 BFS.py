from collections import deque
N,M,V = map(int,input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

def dfs(v):
    visited_dfs[v] = True
    print(v, end=' ')

    graph[v].sort()
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(i)


def bfs(v):
    q = deque([v])
    visited_bfs[v] = True

    while q:
        x = q.popleft()
        print(x, end=' ')
        
        for i in graph[x]:
            if not visited_bfs[i]:
                q.append(i)
                visited_bfs[i] = True


dfs(V)
print('')
bfs(V)
