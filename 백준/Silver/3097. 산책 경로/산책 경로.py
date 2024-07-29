import sys

n = int(input())
l = []
x,y = 0,0
for i in range(n):
    a,b = map(int,input().split())
    x += a
    y += b
    l.append([a,b])

print(x,y)
distance = sys.maxsize

for i in l:
    if ((x-i[0])**2 + (y-i[1])**2)**0.5 < distance:
        distance = ((x-i[0])**2 + (y-i[1])**2)**0.5

print("{:.2f}".format(distance))