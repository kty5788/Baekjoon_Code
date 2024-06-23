n = int(input())
s = set()
for i in range(n):
    name,active = list(input().split())
    if active == 'enter':
        s.add(name)
    else:
        s.remove(name)

ans = sorted(list(s), reverse=True)

for i in ans:
    print(i)