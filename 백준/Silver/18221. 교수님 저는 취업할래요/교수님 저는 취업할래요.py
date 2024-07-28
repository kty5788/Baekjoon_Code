import sys
input = sys.stdin.readline

n = int(input())
l = [[-1],]
for i in range(n):
    l.append([-1]+ list(map(int,input().split())))

other_student = []

for i in range(1, n+1):
    for j in range(1, n+1):
        if l[i][j] == 5:
            professor = [i,j]
        elif l[i][j] == 2:
            sunggyu = [i,j]
        elif l[i][j] == 1:
            other_student.append([i,j])

distance_square = (sunggyu[0]-professor[0])**2 + (sunggyu[1]-professor[1])**2

cnt = 0
for i in other_student:
    if i[0] >= min(sunggyu[0],professor[0]) and i[0] <= max(sunggyu[0],professor[0]) and i[1] >= min(sunggyu[1],professor[1]) and i[1] <= max(sunggyu[1],professor[1]):
        cnt += 1

if distance_square >= 25 and cnt >= 3:
    print(1)
else:
    print(0)