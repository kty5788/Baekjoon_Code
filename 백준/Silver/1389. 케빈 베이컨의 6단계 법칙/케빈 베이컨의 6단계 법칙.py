from collections import deque
N,M = map(int,input().split())
graph = [[] for i in range(N+1)]
res = []

for i in range(M):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1,N+1):
    visited = [0] * (N+1)
    q = deque([i])
    visited[i] = 1

    while q:
        x = q.popleft()

        for j in graph[x]:
            if not visited[j]:
                visited[j] = visited[x] + 1
                q.append(j)
    res.append(sum(visited))

print(res.index(min(res))+1)