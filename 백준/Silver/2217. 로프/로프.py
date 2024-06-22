l = []
k = int(input())
for i in range(k):
    l.append(int(input()))

if len(l) == 1:
    print(l[0]*1)
    exit()

l.sort(reverse=True)

ans = 0
for i in range(len(l)):
    isans = l[-1]*len(l)
    if isans > ans:
        ans = int(isans)
    else:
        l.pop()

print(ans)