from collections import deque
import sys

queue = deque()
n = int(input())
for i in range(n):
    cmd,*b = sys.stdin.readline().strip().split()
    if cmd == 'push':
        queue.appendleft(b[0])
    elif cmd == 'pop':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif cmd == 'front':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif cmd == 'back':
        if queue:
            print(queue[0])
        else:
            print(-1)