k = int(input())
d1,d2 = list(map(int,input().split()))
ans = (k**2 - ((max(d1,d2)-min(d1,d2))*0.5)**2)
print(round(ans,7))