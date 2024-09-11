import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
visited = [False for i in range(10001)]

def bfs(v):
    q = deque([[v,'']])
    while q:
        x,command = q.popleft()
        if not visited[x]:
            visited[x] = True
            calculate = [[(x*2)%10000,'D'],[x-1,'S'],[(x%1000)*10 + x//1000,'L'],[(x%10)*1000 + x//10,'R']]
            
            for i,j in calculate:
                if i < 0:
                    i = 9999
                
                if i == B:
                    return command+j
                else:
                    q.append([i,command+j])

for i in range(t):
    A,B = map(int,input().split())
    print(bfs(A))
    visited = [False for i in range(10001)]