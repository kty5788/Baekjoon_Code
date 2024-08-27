import sys
input = sys.stdin.readline

from collections import deque
M,N = map(int,input().split())
tomato = [list(map(int,input().split())) for  i in range(N)]
visited = [[False for row in range(M)] for col in range(N)]
ripe_tomato = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs():
    q = deque(ripe_tomato)

    while q:
        row,col,day = q.popleft()
        for i in range(4):
            nrow = row + dx[i]
            ncol = col + dy[i]

            if 0 <= ncol < M and 0 <= nrow < N:
                if tomato[nrow][ncol] == 0 and not visited[nrow][ncol]:
                    q.append([nrow,ncol,day+1])
                    visited[nrow][ncol] = True
    
    return day

# 이미 익은 토마토의 위치를 찾아 ripe_tomato 리스트에 추가
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            ripe_tomato.append([i,j,0])
            visited[i][j] = True

# 익은 토마토가 하나도 없다면! -1 출력 / UnboundLocalError 막기 위해 bfs보다 먼저 실행
if not ripe_tomato:
    print(-1)
    exit()

# bfs 알고리즘 함수 실행
res = bfs()

# 도달할 수 없는 익지 않은 토마토가 있는지 확인 / 있다면 -1 출력, 아닐경우 걸린 날짜 출력
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0 and not visited[i][j]:
            print(-1)
            exit()

print(res)