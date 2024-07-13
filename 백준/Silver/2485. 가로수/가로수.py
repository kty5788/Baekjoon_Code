import math
n = int(input())
l = []
numb = []
for i in range(n):
    l.append(int(input()))

for i in range(1,len(l)):
    numb.append(l[i]-l[i-1])

gcd1 = math.gcd(*numb)
cnt = 0
for i in numb:
    cnt += i//gcd1 - 1

print(cnt)