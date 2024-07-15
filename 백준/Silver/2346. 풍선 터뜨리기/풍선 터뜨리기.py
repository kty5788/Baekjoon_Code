from collections import deque
n = int(input())

d = deque(enumerate(map(int,input().split())))
ans = []

while d:
    index,paper = d.popleft()
    ans.append(index+1)

    if paper > 0:
        d.rotate(-(paper-1))
    elif paper < 0:
        d.rotate(-paper)

print(*ans)