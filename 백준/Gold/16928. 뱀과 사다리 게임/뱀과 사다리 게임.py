from collections import deque
n,m = map(int,input().split())
graph = [[] for i in range(101)]
visited = [False for i in range(101)]
for i in range(n+m):
    s,e = map(int,input().split())
    graph[s].append(e)

def bfs():
    q = deque()
    q.append([1,0]) #시작번호 1, 이동횟수 0
    visited[1] = True

    while q:
        num,index = q.popleft()
        for dice in range(1,7):
            if num + dice <= 100:
                if num+dice == 100: # 100 도착하면 횟수 리턴
                    return index+1
                elif graph[num+dice] and not visited[num+dice]: # 사다리 or 뱀이 있다면 타고 올라가기(내려가기)
                    visited[num+dice] = True
                    q.append([graph[num+dice][0],index+1])
                elif not visited[num+dice]: # 아니면 주사위 1-6 만큼 bfs 덱에 추가
                    visited[num+dice] = True
                    q.append([num+dice, index+1])

print(bfs())