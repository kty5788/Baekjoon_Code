import sys
input = sys.stdin.readline

l = []
n = int(input())
for i in range(n):
    x,y,speed = map(int,input().split())
    l.append([i+1,((x**2 + y**2)**0.5)/speed])


l.sort(key= lambda x:x[1])

for i in l:
    print(i[0])

