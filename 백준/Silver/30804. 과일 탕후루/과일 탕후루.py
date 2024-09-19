from collections import defaultdict
 
N = int(input())
arr = list(map(int,input().split()))
 
l,r,cnt = 0,0,0
d = defaultdict(int)
ans = 0

while r < N:
    if d[arr[r]] == 0: # 새로운 과일이 나타날 때 과일 종류(cnt) +1
        cnt += 1
    d[arr[r]] += 1 # 과일 갯수 +1
 
    while cnt > 2: 
        d[arr[l]] -= 1 # 과일의 갯수를 -1, 다만 0(과일이 없음)일 경우 종류 -1
        if d[arr[l]] == 0:
            cnt -= 1
        l += 1
 
    ans = max(ans,r-l+1)
    r += 1
 
print(ans)