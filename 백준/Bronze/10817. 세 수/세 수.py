l = list(map(int,input().split()))

for i in range(1,len(l)):
    key = l[i]
    j = i-1
    while j > -1 and l[j] > key:
        l[j+1] = l[j]
        j -= 1
    l[j+1] = key

print(l[1])
