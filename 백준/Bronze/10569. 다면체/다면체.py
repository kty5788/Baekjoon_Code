t = int(input())
for i in range(t):
    v,e = list(map(int,input().split()))
    ans = 2 - v + e
    print(ans)