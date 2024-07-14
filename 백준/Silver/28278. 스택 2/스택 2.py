import sys
n = int(input())
stack = []
for i in range(n):
    a,*b = map(int,sys.stdin.readline().split())
    if a == 1:
        stack.append(b[0])
    elif a == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif a == 3:
        print(len(stack))
    elif a == 4:
        if stack:
            print(0)
        else:
            print(1)
    elif a == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)