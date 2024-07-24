n,m = map(int,input().split())
if n != 0:
    l = list(map(int,input().split()))
else:
    l = []
now = 0
cnt = 0
for i in l:
    if now+i > m:
        cnt += 1
        now = i
    else:
        now += i

if now != 0:
    cnt += 1

print(cnt)