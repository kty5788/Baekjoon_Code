n = int(input())
l = []
ans = 0
for i in range(n):
    l.append(list(map(int,input().split())))

l.append(l[0])
for i in range(len(l)-1):
    if l[i][0] == l[i+1][0]:
        ans += abs(l[i][1]-l[i+1][1])
    else:
        ans += abs(l[i][0] - l[i+1][0])

print(ans)