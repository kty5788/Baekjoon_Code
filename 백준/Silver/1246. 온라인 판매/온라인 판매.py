n,m = map(int,input().split())
l = []
for i in range(m):
    l.append(int(input()))

l.sort()
ans = []
price = -1
max_amount = -1

for i in range(len(l)):
    if len(l)-i > n:
        max_amount = n
    else:
        max_amount = len(l)-i
    
    if max_amount * l[i] > price:
        price = max_amount*l[i]
        ans.append([l[i],price])


ans = sorted(ans,key= lambda x:-x[1])
print(*ans[0])