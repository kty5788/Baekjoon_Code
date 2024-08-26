from collections import deque
n,k = map(int,input().split())
visited = [False] * 100001


def bfs():
    q = deque([[n,0]])
    visited[n] = True

    while q:
        dot,sec = q.popleft()

        if dot == k:
            return sec
        else:
            if dot+1 <= 100000:
                if visited[dot+1] == False:
                    q.append([dot+1, sec+1])
                    visited[dot+1] = True
            if dot-1 >= 0:
                if visited[dot-1] == False:
                    q.append([dot-1, sec+1])
                    visited[dot-1] = True
            if 2*dot <= 100000:
                if visited[2*dot] == False:
                    q.append([2*dot, sec+1])
                    visited[2*dot] = True

a = bfs()
print(a)