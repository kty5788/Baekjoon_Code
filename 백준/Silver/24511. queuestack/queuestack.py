from collections import deque
n = int(input()) # 자려구조 개수
queuestack = list(map(int,input().split()))
l = list(map(int,input().split()))

m = int(input()) # 수열의 길이
c = list(map(int,input().split()))

res = deque()

for i in range(n):
    if queuestack[i] == 0: # '큐' 이면
        res.append(l[i])

for i in range(m):
    res.appendleft(c[i])
    print(res.pop(), end=' ')
