n = int(input())
l1 = []
l2 = []
for i in range(n):
    l1.append(list(map(int,input().split())))

for i in range(n):
    l2.append(list(map(int,input().split())))

just = []
cnt = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if l1[i][k] == l2[k][j]:
                just.append(l1[i][k])
            else:
                just.append(0)
        if sum(just) != 0:
            cnt += 1
        just.clear()
print(cnt)