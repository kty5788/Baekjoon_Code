from collections import deque
import sys

d = deque()
n = int(input())
for i in range(n):
    cmd,*b = map(int,sys.stdin.readline().strip().split())
    if cmd == 1:
        d.appendleft(b[0])
    elif cmd == 2:
        d.append(b[0])
    elif cmd == 3:
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif cmd == 4:
        if d:
            print(d.pop())
        else:
            print(-1)
    elif cmd == 5:
        print(len(d))
    elif cmd == 6:
        if d:
            print(0)
        else:
            print(1)
    elif cmd == 7:
        if d:
            print(d[0])
        else:
            print(-1)
    elif cmd == 8:
        if d:
            print(d[-1])
        else:
            print(-1)