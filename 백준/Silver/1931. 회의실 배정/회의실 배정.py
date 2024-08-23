import sys
input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    l.append(list(map(int,(input().split()))))

l.sort(key= lambda x : [x[1],x[0]])

cnt = 0
end_time = -1

for i in range(len(l)):
    if end_time == -1:
        end_time = l[i][1]
        cnt += 1
    else:
        if end_time <= l[i][0]:
            end_time = l[i][1]
            cnt += 1

print(cnt)