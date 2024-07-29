n = int(input())
l = list(map(int,input().split()))

res = (l[0]-2)*180

for i in range(1,len(l)):
    res += 180 * l[i]


print(res)