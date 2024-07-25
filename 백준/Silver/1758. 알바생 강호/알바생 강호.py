n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

l.sort(reverse= True)

tips = 0
for i in range(len(l)):
    if l[i]-(i+1-1) >= 0:
        tips += l[i]-(i+1-1)


print(tips)