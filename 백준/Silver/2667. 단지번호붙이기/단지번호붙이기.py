import sys
input = sys.stdin.readline

n = int(input())
house = [list(input()) for i in range(n)]
visited = [[False for row in range(n)] for col in range(n)]

res = 0
house_list = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(i,j,cnt=0):
    stack = []
    stack.append([i,j])
    
    while stack:
        x,y = stack.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and house[nx][ny] != '0':
                    stack.append([nx,ny])
                    visited[nx][ny] = True
                    cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if house[i][j] == '1' and not visited[i][j]:
            num = dfs(i,j)
            if num == 0:
                house_list.append(1)
            else:
                house_list.append(num)
            res += 1

house_list.sort()
print(res)
print(*house_list, sep='\n')