t = int(input())
for i in range(t):
    m,n,x,y = map(int,input().split())
    cnt,k = -1,x
    while k <= m * n:
        if (k - x) % m == 0 and (k - y) % n == 0:
            cnt = k
            break
        k += m
    print(cnt)