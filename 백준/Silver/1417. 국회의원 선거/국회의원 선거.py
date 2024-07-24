n = int(input())
l = []
cnt = 0
dasom = int(input())
for i in range(n-1):
    l.append(int(input()))

l.sort(reverse=True)

if len(l):
    while dasom <= max(l):
        if l[0] >= dasom:
            dasom += 1
            l[0] -= 1
            cnt += 1
            l.sort(reverse=True)

print(cnt)