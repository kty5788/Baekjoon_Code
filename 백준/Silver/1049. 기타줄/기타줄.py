n,m = map(int,input().split())
l = []
for i in range(m):
    l.append(list(map(int,input().split())))

min_pack,min_each = 1001,1001
for i in l:
    if i[0] < min_pack:
        min_pack = i[0]
    
    if i[1] < min_each:
        min_each = i[1]

price = 0
while n > 0:
    if n >= 6:
        if min_pack > min_each * 6:
            price += min_each*6
        else:
            price += min_pack
        n -= 6
    else:
        if min_pack > min_each * n:
            price += min_each * n
        else:
            price += min_pack
        n = 0

print(price)