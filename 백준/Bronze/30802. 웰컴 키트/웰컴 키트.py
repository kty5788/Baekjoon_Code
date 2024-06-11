n = int(input())
size = list(map(int,input().split()))
t,p = list(map(int,input().split()))
cnt = 0

for i in size:
    cnt += i//t
    i %= t
    if i != 0:
        cnt += 1
print(cnt)
print(n//p,n%p)