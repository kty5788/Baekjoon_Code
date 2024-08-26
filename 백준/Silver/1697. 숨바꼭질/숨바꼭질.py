import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
visited = [False] * 100001


def bfs():
    q = deque([[n,0]])
    visited[n] = True

    while q:
        dot,sec = q.popleft()

        if dot == k: # 위치가 같다면 리턴
            return sec
        else: # 아닐 경우
            for i in [dot+1, dot-1, 2*dot]:
                if 0 <= i <= 100000 and not visited[i]:
                    q.append([i,sec+1])
                    visited[i] = True

ans = bfs()
print(ans)