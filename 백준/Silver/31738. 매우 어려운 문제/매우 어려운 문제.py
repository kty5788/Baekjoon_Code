n,m = map(int,input().split())
res = 1

if n >= m:
    print(0)
    exit()

for i in range(2,n+1):
    res *= i
    res %= m
    if res == 0:
        break

print(res%m)